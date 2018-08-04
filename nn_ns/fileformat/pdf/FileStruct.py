
'''
InitialPdf_old = Header Body CrossReferenceTable Trailer
InitialPdf_new = Header Body "startxref" EOL Offset EOL "%%EOF"
    -- may use CrossReferenceStream instead of ~Table
    -- more -> hybrid-reference /XRefStm
Pdf_old = Header (Body CrossReferenceTable Trailer)+
Header = "%PDF-" PInt '.' UInt
Body = IndirectObjDef
CrossReferenceTable = CrossReferenceSection+
CrossReferenceSection = "xref" EOL CrossReferenceSubsection+
CrossReferenceSubsection = ObjNum ' ' UInt EOL CrossReferenceEntry*
    -- first obj num ; size
    contiguous range of object numbers
    first CrossReferenceSubsection for every CrossReferenceSection
        numbering begins at 0
CrossReferenceEntry = byte{20} & (InUseEntry | FreeEntry)
    global first CrossReferenceEntry
        "0000000000 65535 f" PadEOL
        it is head of free list
        tail of free list link back to it
    first CrossReferenceEntry for every CrossReferenceSubsection
        nextObjNum ' ' 65535 f" PadEOL
PadEOL = ' ' Newline | CR LF
InUseEntry = \d{10} ' ' \d{5} " n" PadEOL
    -- offset GenNum
FreeEntry  = \d{10} ' ' \d{5} " f" PadEOL
    -- ObjNum-of-next-free-obj GenNum-of-this-objNum-as-newGenNum


Trailer = "trailer" Dict EOL "startxref" EOL Offset EOL "%%EOF"
    -- offset of "xref"
    -- how to read pdf?
    --      -- take care of Comment
    --      -- we should search newline from back to front
    --      from end of file -> read offset of xref
    --      -> read xref -> read trailer_dict -> read /Size
    --          -- we read xref before read /Size!!!
    --      -> read /Prev? for prev xref -- old data as prototype
Offset = UInt



-- example:
type CrossReferenceTableT = [CrossReferenceEntryT]
data CrossReferenceEntryT
    = InUseEntryT Offset GenNum | FreeEntryT NextObjNum ThisGenNum
readObjRef
    :: (ObjNum, GenNum) -> CrossReferenceTableT -> Maybe Offset
readObjRef (objNum, genNum) table = case index objNum table of
    FreeEntryT _ _ -> Nothing
    InUseEntryT offset g' -> if g' /= genNum then Nothing else
        Just offset
deleteObjRef
    :: (ObjNum, GenNum) -> CrossReferenceTableT -> CrossReferenceTableT
deleteObjRef (objNum, genNum) table = case index objNum table of
    FreeEntryT _ _ -> table
    InUseEntryT offset g' = if g' /= genNum then table else
        update this thisEntry' $ update 0 entry0' table where
        -- value@i   <==>   value == index i table
        -- old free list = top@0 -> ?x@top -> ...a@b -> c@a... -> 0@?y
        -- new free list = this@0 -> top@this -> ?x@top -> ... -> 0@?y
        max = 65535
        this = objNum
        entry0@(FreeEntryT old_top 65535) = head table
        entry0' = FreeEntryT this 65535
        thisEntry' = FreeEntryT old_top $ genNum+1 -- overflow??
        -- assert genNum /= max
reuseObjRef
    -- Nothing means no existed objNum can be reused
    --      we have to add new objNum
    :: Offset -> CrossReferenceTableT
    -> Maybe (ObjNum, GenNum, CrossReferenceTableT) -- genNum < max
reuseObjRef offset table =
    case find (-1) (-1) 0 of
        Nothing -> Nothing
        -- old: ... -> (i, pg)@parent -> (child, g)@i -> (...)@child->...
        -- new: ... -> (child, pg)@parent -> (...)@child->...
        Just (parent, pg, i, g) -> assert (parent != -1) $
            let table' = update i (InUseEntryT offset g) $
                         update parent (FreeEntryT child pg) table
            in Just (i, g, table')
  where
    find parent parentGenNum i =
        -- i == 0 ==>> g == max
            if g < max then Just (parent, parentGenNum, i,g) else
            if child == 0 then Nothing else
            find i g child where
                FreeEntryT child g = index i table

'''
