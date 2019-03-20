

{-# LANGUAGE TypeFamilies #-}
{-# LANGUAGE FunctionalDependencies #-}
{-# LANGUAGE TypeFamilyDependencies #-}
{-# LANGUAGE GeneralizedNewtypeDeriving #-}
{-# LANGUAGE ExplicitForAll #-}
{-# LANGUAGE ScopedTypeVariables #-}
{-# LANGUAGE TypeApplications #-}
{-# LANGUAGE AllowAmbiguousTypes #-}


{-
{-# LANGUAGE TemplateHaskell #-}
{-# LANGUAGE TypeSynonymInstances #-}
{-# LANGUAGE MultiParamTypeClasses #-}
{-# LANGUAGE UndecidableSuperClasses #-}
{-# LANGUAGE UndecidableInstances #-}
{-# LANGUAGE FlexibleContexts #-}
{-# LANGUAGE FlexibleInstances #-}
-}
{-
see:
    "[A001203]pi.txt"
        matrix as linear fractional transformation
    https://www.cs.ox.ac.uk/jeremy.gibbons/publications/spigot.pdf
        "Unbounded Spigot Algorithms for the Digits of Pi (2006)(Gibbons).pdf"


    usage:
        constant_outputs = the_constant_outputs_ @StreamingAlgorithmState4Pi_by_???
        float_part_number_convertor (mkRadixBaseFloatPartNumber baseI [???]) baseO


-}

module StreamingAlgorithm
    (Callable(..)
    ,StreamingAlgorithm(..)
    ,streaming
    ,LinearFractionalTransformation(..)
    -- ,call_LinearFractionalTransformation
    ,RadixBases4Convert(..)
    ,FloatPartRadixBaseConvertorState(..)

    ,RadixBaseFloatPartNumber() -- Nothing
    ,unRadixBaseFloatPartNumber
    ,mkRadixBaseFloatPartNumber
    ,finite_maybe_mkRadixBaseFloatPartNumber
    ,float_part_number_convertor
    -- ,float_part_digits_convertor
    ,finite_float_part_number2rational
    -- ,finite_float_part_digits2rational

    ,Label(..)
    ,unLabel
    ,ConstantStreamingAlgorithm(..)
    ,the_constant_outputs
    ,the_constant_inputs_
    ,the_constant_outputs_
    ,StreamingAlgorithmState4Pi_by_Rabinowitz_and_Wagon__base10
    ,StreamingAlgorithmState4Pi_by_Lambert__base10
    ,StreamingAlgorithmState4Pi_by_Gosper__base10
    )
where

--import Control.Category
--  ==>> Monoid
import Control.Exception(assert)
import Data.Semigroup
-- import Data.Traversable (forM)
import Control.Monad (forM_, unless, when, guard, mzero)
import Data.List (zip4)

class Callable a where
    type InputType4Callable a :: *
    type OutputType4Callable a :: *
    call :: a -> InputType4Callable a -> OutputType4Callable a

class StreamingAlgorithm state where
    {- # MINIMAL
            update_after_consume
            , (maybe_poll | maybe_peek, unsafe_update_after_poll)
        # -}

    type OutputType4StreamingAlgorithm state :: *
    type InputType4StreamingAlgorithm state :: *

    maybe_poll
        :: state -> Maybe (state, OutputType4StreamingAlgorithm state)
    update_after_consume
        :: state -> InputType4StreamingAlgorithm state -> state

    {-
    type PseudoOutputType4StreamingAlgorithm state :: *
    pseudo_peek
        :: state -> PseudoOutputType4StreamingAlgorithm state
    pseudo_output2maybe_output
        :: state -> PseudoOutputType4StreamingAlgorithm state
        -> Maybe (OutputType4StreamingAlgorithm state)
    -}

    {-
    maybe_peek
        :: state -> Maybe (OutputType4StreamingAlgorithm state)
    unsafe_update_after_poll
        :: state -> OutputType4StreamingAlgorithm state -> state

    maybe_poll state = do
        output <- maybe_peek state
        return $ (unsafe_update_after_poll state output, output)
    maybe_peek state = do
        (state', output) <- maybe_poll state
        return output
    unsafe_update_after_poll state output
        = maybe undefined fst $ maybe_poll state
    -}

streaming
    :: StreamingAlgorithm state
    => state -> [InputType4StreamingAlgorithm state]
    -> [OutputType4StreamingAlgorithm state]
streaming state inputs = case maybe_poll state of
    Just (state', output) -> output : streaming state' inputs
    Nothing -> case inputs of
        (h:inputs') -> streaming (update_after_consume state h) inputs'
        [] -> []


data LinearFractionalTransformation
    = LinearFractionalTransformation
        {up_left :: Integer
        ,up_right :: Integer
        ,down_left :: Integer
        ,down_right :: Integer
        }
        deriving (Read, Show)
    {-
    matrix[ul, ur; dl, dr](x) = (ul*x+ur)/(dl*x+dr)
    I = matrix[1,0; 0,1]
    I(x) = (1*x+0)/(0*x+1) = x
    -}


-- call_LinearFractionalTransformation :: LinearFractionalTransformation -> Rational -> Rational
instance Callable LinearFractionalTransformation where
    type InputType4Callable LinearFractionalTransformation = Rational
    type OutputType4Callable LinearFractionalTransformation = Rational
    call
        LinearFractionalTransformation
            {up_left=ul, up_right=ur, down_left=dl, down_right=dr}
        x = f ul ur x / f dl dr x
        where
            f l r x = toRational l * x + toRational r

instance Semigroup LinearFractionalTransformation where
    (<>) = mappend
instance Monoid LinearFractionalTransformation where
    mempty = LinearFractionalTransformation
        {up_left=1, up_right=0, down_left=0, down_right=1}

    mappend
        LinearFractionalTransformation
            {up_left=ul, up_right=ur, down_left=dl, down_right=dr}
        LinearFractionalTransformation
            {up_left=ul', up_right=ur', down_left=dl', down_right=dr'}
        = LinearFractionalTransformation
            {up_left  =ul*ul' + ur*dl', up_right  =ul*ur' + ur*dr'
            ,down_left=dl*ul' + dr*dl', down_right=dl*ur' + dr*dr'
            }


data RadixBases4Convert
    = RadixBases4Convert
        {from_radix_base :: Integer
        ,to_radix_base :: Integer
        }
        deriving (Read, Show)
data FloatPartRadixBaseConvertorState
    = FloatPartRadixBaseConvertorState
        {radix_bases4convert :: RadixBases4Convert
        ,outer_mul_number :: Rational
        ,inner_add_number :: Rational
        }
        deriving (Read, Show)

instance StreamingAlgorithm FloatPartRadixBaseConvertorState where
    {-
    float_point_number :: (radix_base, [digit])
        0 <= digit < radix_base
        to_float_point_number radix_base digits
            = 1/radix_base * (digits[0] + 1/radix_base * (...))
            = II matrix[1/radix_base, digits[i]/radix_base; 0, 1] {i <- 0}

        [how (radix_base, radix_base', digits) -> digits']?
            [to_float_point_number radix_base digits == to_float_point_number radix_base' digits']
            to_float_point_number radix_base digits
            = 1/radix_base * (digits[0] + 1/radix_base * (...))
            = 1/radix_base' * (digits'[0] + 1/radix_base' * (...))

            # streaming
            # let remain[i] = to_float_point_number radix_base digits[i:]
            #   remain[i] = 1/radix_base * (digits[i] + remain[i+1])
            # let tail[j,i] = u[j,i]*(v[j,i] + remain[i])
            # let head[j](tail) = 1/radix_base' * (digits'[0] + 1/radix_base' * (...(digits'[j] + tail)))
            = head[j](tail[j,i])

            # consume; not output; consume first
            = head[j](tail[j,i+1])
                #tail[j,i] == tail[j,i+1]
            # poll; 1 more output; not consume input
            = head[j+1](tail[j+1,i])
                #tail[j,i]*radix_base' == digits'[j+1] + tail[j+1,i]
                #                           floor       float_part

            # init
            = head[-1](tail[-1,0])
            ==>>
                u[-1,0] == 1
                v[-1,0] == 0

            ==>>
                [@j,i: tail[j,i] <= 1]
                # NOTE: [0.9999... == 1]
            ==>>
                * poll
                    j' = j+1
                    i' = i
                    digits'[j+1] = floor(tail[j,i]*radix_base')
                    tail[j,i] = u[j,i]*(v[j,i] + remain[i])
                    0 <= remain[i] <= 1
                    # we donot know tail[j,i], but we know its range:
                    u[j,i]*v[j,i] <= tail[j,i] <= u[j,i]*(v[j,i]+1)
                    lower_bound = u[j,i]*v[j,i]*radix_base'
                    upper_bound = u[j,i]*(v[j,i]+1)*radix_base'
                    digits'[j+1] <- [floor lower_bound .. floor upper_bound]
                * consume
                    j' = j
                    i' = i+1
                ???[poll or consume]???
                    consume first
                        if floor lower_bound == floor upper_bound:
                            #poll
                            D' = digits'[j+1] = floor lower_bound
                            tail[j,i]
                                = u[j,i]*(v[j,i] + remain[i])
                                = 1/radix_base'*(D' + u[j+1,i]*(v[j+1,i] + remain[i]))
                            # coeff of remain[i]
                            u[j,i] = 1/radix_base'*u[j+1,i]
                            u[j+1,i] = u[j,i]*radix_base'
                            # not coeff of remain[i]
                            u[j,i]*v[j,i]
                            = 1/radix_base'*(D' + u[j+1,i]*v[j+1,i])
                            u[j+1,i]*v[j,i] = D' + u[j+1,i]*v[j+1,i]
                            v[j+1,i] = v[j,i] - D'/u[j+1,i]

                            ==>>
                            D' = digits'[j+1] = floor lower_bound
                            u[j+1,i] = u[j,i]*radix_base'
                            v[j+1,i] = v[j,i] - D'/u[j+1,i]
                        else:
                            #consume
                            tail[j,i] = u[j,i]*(v[j,i] + remain[i])
                            = tail[j,i+1] = u[j,i+1]*(v[j,i+1] + remain[i+1])
                            remain[i] = 1/radix_base * (digits[i] + remain[i+1])
                            D = digits[i]
                            # coeff of remain[i+1]
                            u[j,i]*1/radix_base = u[j,i+1]
                            u[j,i+1] = u[j,i]/radix_base
                            # not coeff of remain[i+1]
                            u[j,i]*(v[j,i]+1/radix_base * D) = u[j,i+1]*v[j,i+1]
                            u[j,i]*v[j,i]+ u[j,i+1]*D = u[j,i+1]*v[j,i+1]
                            v[j,i+1] = u[j,i]*v[j,i]/u[j,i+1] + D
                            v[j,i+1] = radix_base*v[j,i] + D

                            ==>>
                            D = digits[i]
                            u[j,i+1] = u[j,i]/radix_base
                            v[j,i+1] = v[j,i]*radix_base + D

    -}

    type OutputType4StreamingAlgorithm FloatPartRadixBaseConvertorState = Integer
    type InputType4StreamingAlgorithm FloatPartRadixBaseConvertorState = Integer

    -- maybe_poll :: state -> Maybe (state, OutputType4StreamingAlgorithm state)
    maybe_poll
        FloatPartRadixBaseConvertorState
            {radix_bases4convert
                =bases@RadixBases4Convert
                    {from_radix_base=baseI, to_radix_base=baseO}
            ,outer_mul_number=u
            ,inner_add_number=v
            }
        = if ok then Just (state', d') else Nothing
        where
            baseO_r = toRational baseO
            lower_bound = u*v*baseO_r
            upper_bound = lower_bound + u*baseO_r
            lower_digit, upper_digit :: Integer
            lower_digit = floor lower_bound
            upper_digit = floor upper_bound
            ok = lower_digit == upper_digit

            -- if ok, poll
            -- poll
            {-
            D' = digits'[j+1] = floor lower_bound
            u[j+1,i] = u[j,i]*radix_base'
            v[j+1,i] = v[j,i] - D'/u[j+1,i]
            -}
            d' = lower_digit
            u' = u*baseO_r
            v' = v - (toRational d')/u'
            state' = FloatPartRadixBaseConvertorState
                {radix_bases4convert=bases
                ,outer_mul_number=u'
                ,inner_add_number=v'
                }


    -- update_after_consume :: state -> InputType4StreamingAlgorithm state -> state
    update_after_consume
        FloatPartRadixBaseConvertorState
            {radix_bases4convert
                =bases@RadixBases4Convert
                    {from_radix_base=baseI, to_radix_base=baseO}
            ,outer_mul_number=u
            ,inner_add_number=v
            }
        input_digit
        = state'
        where
            baseI_r = toRational baseI
            -- consume
            {-
            D = digits[i]
            u[j,i+1] = u[j,i]/radix_base
            v[j,i+1] = v[j,i]*radix_base + D
            -}
            d = input_digit
            u' = u/baseI_r
            v' = v*baseI_r + (toRational d)
            state' = FloatPartRadixBaseConvertorState
                {radix_bases4convert=bases
                ,outer_mul_number=u'
                ,inner_add_number=v'
                }

-- ----------------------------------
finite_float_part_digits2rational :: Integer -> [Integer] -> Rational
finite_float_part_digits2rational baseI input_float_part_digits
    = output_rational
    where
        output_rational = f input_float_part_digits
        baseI_r = toRational baseI
        f (h:ts) = (toRational h + f ts) / baseI_r
        f [] = 0


data RadixBaseFloatPartNumber
    = RadixBaseFloatPartNumber
        {radix_base :: Integer
        ,float_part_digits :: [Integer]
            -- maybe infinite
        }
        deriving (Read, Show)

unRadixBaseFloatPartNumber :: RadixBaseFloatPartNumber -> (Integer, [Integer])
mkRadixBaseFloatPartNumber :: Integer -> [Integer] -> RadixBaseFloatPartNumber
finite_maybe_mkRadixBaseFloatPartNumber :: Integer -> [Integer] -> Maybe RadixBaseFloatPartNumber

unRadixBaseFloatPartNumber
    RadixBaseFloatPartNumber
        {radix_base=radix_base
        ,float_part_digits=float_part_digits
        }
    = (radix_base, float_part_digits)

finite_maybe_mkRadixBaseFloatPartNumber radix_base float_part_digits
    = if radix_base >= 2 && all is_ok float_part_digits
    then return $ RadixBaseFloatPartNumber
        {radix_base = radix_base
        ,float_part_digits = float_part_digits
        }
    else Nothing
    where
        is_ok x = (0<=x && x <radix_base)

mkRadixBaseFloatPartNumber radix_base float_part_digits
    = RadixBaseFloatPartNumber
        {radix_base = radix_base'
        ,float_part_digits = float_part_digits'
        }
    where
        radix_base' = assert (radix_base >= 2) radix_base
        float_part_digits' = do
            -- maybe infinite
            x <- float_part_digits
            return $ assert (0<=x && x <radix_base') x

finite_float_part_number2rational :: RadixBaseFloatPartNumber -> Rational
float_part_number_convertor :: RadixBaseFloatPartNumber -> Integer -> [Integer]

finite_float_part_number2rational
    RadixBaseFloatPartNumber
        {radix_base=radix_base
        ,float_part_digits=float_part_digits
        }
    = finite_float_part_digits2rational radix_base float_part_digits

float_part_number_convertor
    RadixBaseFloatPartNumber
        {radix_base=baseI
        ,float_part_digits=float_part_digits
        }
    baseO
    = float_part_digits_convertor (baseI, float_part_digits) baseO


float_part_digits_convertor :: (Integer, [Integer]) -> Integer -> [Integer]
float_part_digits_convertor (baseI, input_float_part_digits) baseO
    = output_float_part_digits
    where
        state0 = FloatPartRadixBaseConvertorState
            {radix_bases4convert
                =RadixBases4Convert
                    {from_radix_base=baseI, to_radix_base=baseO}
                {-
                u[-1,0] == 1
                v[-1,0] == 0
                -}
            ,outer_mul_number=1
            ,inner_add_number=0
            }
        output_float_part_digits = streaming state0 input_float_part_digits

e_base3 = [1,0,0,2,2,1,0,1,1,2]
e_base7 = [2,4,0,1,1,6,4,3,5,2]
main1__radix_base_convert :: IO ()
main1__radix_base_convert = do
    print "e_base3 -> e_base7"
    print e_base7
    print $ float_part_digits_convertor (3, e_base3) 7
    print $ float_part_number_convertor (mkRadixBaseFloatPartNumber 3 e_base3) 7

    print "e_base7 -> e_base3"
    print e_base3
    print $ float_part_digits_convertor (7, e_base7) 3
    print $ float_part_number_convertor (mkRadixBaseFloatPartNumber 7 e_base7) 3

-- ----------------------------




newtype Label label a = Label a
    deriving (Show, Read)
unLabel :: forall label a. Label label a -> a
unLabel (Label a) = a

class StreamingAlgorithm state => ConstantStreamingAlgorithm state where
    the_initial_state :: state
    the_constant_inputs :: Label state [InputType4StreamingAlgorithm state]


the_constant_inputs_
    :: forall state. ConstantStreamingAlgorithm state
    => [InputType4StreamingAlgorithm state]
the_constant_outputs_
    :: forall state. ConstantStreamingAlgorithm state
    => [OutputType4StreamingAlgorithm state]
the_constant_inputs_ = unLabel $ the_constant_inputs @state
the_constant_outputs_ = unLabel $ the_constant_outputs @state

the_constant_outputs
    :: forall state. ConstantStreamingAlgorithm state
    => Label state [OutputType4StreamingAlgorithm state]
the_constant_outputs = Label constant_outputs
    where
        initial_state = (the_initial_state
            :: forall. state)
        Label constant_inputs = (the_constant_inputs
            :: forall. Label state [InputType4StreamingAlgorithm state])
        constant_outputs = (streaming initial_state constant_inputs
            :: forall. [OutputType4StreamingAlgorithm state])








_subtract_then_lshift :: Integer -> Integer -> LinearFractionalTransformation
    {-
        assume
            remain = digit + remain_
            remain' = radix_base*remain_
        digit :: Integer
        0 <= digit < radix_base
        0 <= remain' < 1
        digit = floor remain
        remain' = radix_base*(remain - floor remain)
            = radix_base*remain + (-radix_base*digit)

        ==>> matrix[radix_base, -radix_base*digit; 0, 1]
    -}
_subtract_then_lshift radix_base digit =
        LinearFractionalTransformation
        {up_left = radix_base
        ,up_right = -radix_base*digit
        ,down_left = 0
        ,down_right = 1
        }



newtype StreamingAlgorithmState4Pi_by_Rabinowitz_and_Wagon__base10
    = StreamingAlgorithmState4Pi_by_Rabinowitz_and_Wagon__base10
        LinearFractionalTransformation
    deriving (Show, Read, Monoid, Semigroup)


instance Callable StreamingAlgorithmState4Pi_by_Rabinowitz_and_Wagon__base10 where
    type InputType4Callable StreamingAlgorithmState4Pi_by_Rabinowitz_and_Wagon__base10 = Rational
        -- = InputType4Callable LinearFractionalTransformation
    type OutputType4Callable StreamingAlgorithmState4Pi_by_Rabinowitz_and_Wagon__base10 = Rational
        -- = OutputType4Callable LinearFractionalTransformation
    call (StreamingAlgorithmState4Pi_by_Rabinowitz_and_Wagon__base10 matrix) = call matrix

instance StreamingAlgorithm StreamingAlgorithmState4Pi_by_Rabinowitz_and_Wagon__base10 where
    type OutputType4StreamingAlgorithm StreamingAlgorithmState4Pi_by_Rabinowitz_and_Wagon__base10
        = Integer
    type InputType4StreamingAlgorithm StreamingAlgorithmState4Pi_by_Rabinowitz_and_Wagon__base10
        = StreamingAlgorithmState4Pi_by_Rabinowitz_and_Wagon__base10

    -- maybe_poll :: state -> Maybe (state, OutputType4StreamingAlgorithm state)
    maybe_poll state = if ok then Just (state', digit') else Nothing
        where
            lower_digit = floor $ call state 3
            upper_digit = floor $ call state 4

            ok = lower_digit == upper_digit
            -- if ok
            digit' = lower_digit
            -- digit' = floor remain
            -- remain' = 10*(remain-digit') = 10*(remain) + -10*digit'
            state' = subtract_then_lshift' <> state
            subtract_then_lshift' = StreamingAlgorithmState4Pi_by_Rabinowitz_and_Wagon__base10
                $ _subtract_then_lshift 10 digit'
    -- update_after_consume :: state -> InputType4StreamingAlgorithm state -> state
    update_after_consume state next_matrix = state <> next_matrix
instance ConstantStreamingAlgorithm StreamingAlgorithmState4Pi_by_Rabinowitz_and_Wagon__base10 where
    the_initial_state = mempty
    the_constant_inputs = Label $ do
        k <- [1..]
        let dr = 2*k+1
        return . StreamingAlgorithmState4Pi_by_Rabinowitz_and_Wagon__base10 $
            LinearFractionalTransformation
                {up_left=k, up_right=2*dr, down_left=0, down_right=dr}

main2__pi__Rabinowitz_and_Wagon_spigot :: IO ()
main2__pi__Rabinowitz_and_Wagon_spigot = do
    print "decimal digit of pi Rabinowitz_and_Wagon_spigot"
    print $ take 100 constant_outputs where
        -- Label constant_outputs = (the_constant_outputs :: Label StreamingAlgorithmState4Pi_by_Rabinowitz_and_Wagon__base10 [Integer])
        constant_outputs = the_constant_outputs_ @StreamingAlgorithmState4Pi_by_Rabinowitz_and_Wagon__base10



-- --------------------------------

data StreamingAlgorithmState4Pi_by_Lambert__base10
    = StreamingAlgorithmState4Pi_by_Lambert__base10
        LinearFractionalTransformation -- matrix
        Integer -- input_position/input_index
    deriving (Show, Read)



instance StreamingAlgorithm StreamingAlgorithmState4Pi_by_Lambert__base10 where
    type OutputType4StreamingAlgorithm StreamingAlgorithmState4Pi_by_Lambert__base10
        = Integer
    type InputType4StreamingAlgorithm StreamingAlgorithmState4Pi_by_Lambert__base10
        = LinearFractionalTransformation

    -- maybe_poll :: state -> Maybe (state, OutputType4StreamingAlgorithm state)
    maybe_poll (StreamingAlgorithmState4Pi_by_Lambert__base10
                    state_mx input_idx)
        = if ok then Just (state', digit') else Nothing
        where
            k_r = toRational input_idx
            lower_digit = floor $ call state_mx (2*k_r-1)
            upper_digit = floor $ call state_mx (2*k_r-1+k_r/2)

            ok = lower_digit == upper_digit
            -- if ok
            digit' = lower_digit
            -- digit' = floor remain
            -- remain' = 10*(remain-digit') = 10*(remain) + -10*digit'
            state_mx' = subtract_then_lshift' <> state_mx
            subtract_then_lshift' = _subtract_then_lshift 10 digit'
            state' = StreamingAlgorithmState4Pi_by_Lambert__base10
                state_mx' input_idx
    -- update_after_consume :: state -> InputType4StreamingAlgorithm state -> state
    update_after_consume
        (StreamingAlgorithmState4Pi_by_Lambert__base10
            state_mx input_idx)
        next_input_mx
        = state'
        where
            state' = StreamingAlgorithmState4Pi_by_Lambert__base10
                state_mx' input_idx'
            state_mx' = state_mx <> next_input_mx
            input_idx' = input_idx+1

instance ConstantStreamingAlgorithm StreamingAlgorithmState4Pi_by_Lambert__base10 where
    the_initial_state
        = StreamingAlgorithmState4Pi_by_Lambert__base10 state_mx input_idx
        where
            state_mx = LinearFractionalTransformation
                {up_left=0, up_right=4, down_left=1, down_right=0}
            input_idx = 1

    the_constant_inputs = Label $ do
        input_idx <- [1..]
        let k = input_idx
        return LinearFractionalTransformation
            {up_left=2*k-1, up_right=k^2, down_left=1, down_right=0}

    {-
    # Lambert_expression
    pi = 4/(1+1^2/(3+2^2/(5+3^2/(7+...))))
        = 4/( (1+1^2/) (3+2^2/) (5+3^2/) ... )
        = 4 / II (2*k-1 + k^2/) {k <- 1...}
        = matrix[0, 4; 1, 0] * II matrix[2*k-1, k^2; 1, 0] {k <- 1..}
        #pi === 4/Lambert_expression(1)
        #???Lambert_expression(k) <- range[2*k-1, 2*k-1+k/2]
        fact: st(2*k-1) <= digit <= st(2*k-1+k/2)
    -}



main3__pi__Lambert :: IO ()
main3__pi__Lambert = do
    print "decimal digit of pi Lambert"
    print $ take 100 constant_outputs where
        -- Label constant_outputs = (the_constant_outputs :: Label StreamingAlgorithmState4Pi_by_Lambert__base10 [Integer])
        constant_outputs = the_constant_outputs_ @StreamingAlgorithmState4Pi_by_Lambert__base10





-- --------------------------------

data StreamingAlgorithmState4Pi_by_Gosper__base10
    = StreamingAlgorithmState4Pi_by_Gosper__base10
        LinearFractionalTransformation -- matrix
        Integer -- input_position/input_index
    deriving (Show, Read)



instance StreamingAlgorithm StreamingAlgorithmState4Pi_by_Gosper__base10 where
    type OutputType4StreamingAlgorithm StreamingAlgorithmState4Pi_by_Gosper__base10
        = Integer
    type InputType4StreamingAlgorithm StreamingAlgorithmState4Pi_by_Gosper__base10
        = LinearFractionalTransformation

    -- maybe_poll :: state -> Maybe (state, OutputType4StreamingAlgorithm state)
    maybe_poll (StreamingAlgorithmState4Pi_by_Gosper__base10
                    state_mx input_idx)
        = if ok then Just (state', digit') else Nothing
        where
            k_r = toRational input_idx
            _27_5 = toRational 27 / 5
            _12_5 = toRational 12 / 5
            _6_5_3 = (toRational 6 / 5)^3
            -- 27/5 * k - 12/5
            -- 27/5 * k - (6/5)^3
            lower_digit = floor $ call state_mx (_27_5*k_r-_12_5)
            upper_digit = floor $ call state_mx (_27_5*k_r-_6_5_3)

            ok = lower_digit == upper_digit
            -- if ok
            digit' = lower_digit
            -- digit' = floor remain
            -- remain' = 10*(remain-digit') = 10*(remain) + -10*digit'
            state_mx' = subtract_then_lshift' <> state_mx
            subtract_then_lshift' = _subtract_then_lshift 10 digit'
            state' = StreamingAlgorithmState4Pi_by_Gosper__base10
                state_mx' input_idx
    -- update_after_consume :: state -> InputType4StreamingAlgorithm state -> state
    update_after_consume
        (StreamingAlgorithmState4Pi_by_Gosper__base10
            state_mx input_idx)
        next_input_mx
        = state'
        where
            state' = StreamingAlgorithmState4Pi_by_Gosper__base10
                state_mx' input_idx'
            state_mx' = state_mx <> next_input_mx
            input_idx' = input_idx+1

instance ConstantStreamingAlgorithm StreamingAlgorithmState4Pi_by_Gosper__base10 where
    the_initial_state
        = StreamingAlgorithmState4Pi_by_Gosper__base10 state_mx input_idx
        where
            state_mx = mempty
            input_idx = 1

    the_constant_inputs = Label $ do
        input_idx <- [1..]
        let k = input_idx
            kkk = 3*(3*k+1)*(3*k+2)
        return LinearFractionalTransformation
            {up_left=k*(2*k-1), up_right=kkk*(5*k-2)
            ,down_left=0, down_right=kkk
            }

    {-
    # Gosper_series
    pi = 3 + (1*1)/(3*4*5) * (8 + (2*3)/(3*7*8) * (...(5*k-2) + (k*(2*k-1))/(3*(3*k+1)*(3*k+2)) * (...)))
        = (3 + (1*1)/(3*4*5) *) (8 + (2*3)/(3*7*8) *) ... ((5*k-2) + (k*(2*k-1))/(3*(3*k+1)*(3*k+2)) *) ...
        = II ((5*k-2) + (k*(2*k-1))/(3*(3*k+1)*(3*k+2)) *) {k <- 1..}
        = II matrix[(k*(2*k-1), 3*(3*k+1)*(3*k+2)*(5*k-2); 0, 3*(3*k+1)*(3*k+2)] {k <- 1..}
        #pi === Gosper_series(1)
        #???Gosper_series(k) <- [27/5 * k - 12/5, 27/5 * k - (6/5)^3]
        ???fact: st(27/5 * k - 12/5) <= digit <= st(27/5 * k - (6/5)^3)
        ???fact: st(27/5 * (k+1) - 12/5) <= digit <= st(27/5 * (k+1) - (6/5)^3)
        st(27/5 * k - 12/5) = matrix[q,r;s,t](27/5 * k - 12/5)
            = matrix[q,5*r;s,5*t](27*k - 12)
        st(27/5 * (k+1) - 12/5)
            = matrix[q,5*r;s,5*t](27*(k+1) - 12)
            = matrix[q,5*r;s,5*t](27*k + 15)
        st(27/5 * k - (6/5)^3) = matrix[q,r;s,t](27/5 * k - 216/125)
            = matrix[q,125*r;s,125*t](675*k - 216)


    -}



main4__pi__Gosper :: IO ()
main4__pi__Gosper = do
    print "decimal digit of pi Gosper"
    print $ take 100 constant_outputs where
        -- Label constant_outputs = (the_constant_outputs :: Label StreamingAlgorithmState4Pi_by_Gosper__base10 [Integer])
        constant_outputs = the_constant_outputs_ @StreamingAlgorithmState4Pi_by_Gosper__base10





-- -------------------------------
main :: IO ()
main = do
    main1__radix_base_convert
    main2__pi__Rabinowitz_and_Wagon_spigot
    main3__pi__Lambert
    main4__pi__Gosper

    let constant_outputs_RW = the_constant_outputs_ @StreamingAlgorithmState4Pi_by_Rabinowitz_and_Wagon__base10
        constant_outputs_L = the_constant_outputs_ @StreamingAlgorithmState4Pi_by_Lambert__base10
        constant_outputs_G = the_constant_outputs_ @StreamingAlgorithmState4Pi_by_Gosper__base10
        -- triples = zip3 constant_outputs_RW constant_outputs_L constant_outputs_G
        tuple4s = zip4 [0..] constant_outputs_RW constant_outputs_L constant_outputs_G

    {-
    print "guard True"
    guard True
    print "guard False"
    guard False
    -}

    forM_ tuple4s $ \tuple4@(i, a, b, c) -> do
        -- unless (a == b && b == c) $ print tuple4
        -- if (a == b && b == c) then print i else print tuple4
        --
        -- guard (a == b && b == c)
        -- print i
        --
        if (a == b && b == c) then print i else do
            print tuple4
            mzero


