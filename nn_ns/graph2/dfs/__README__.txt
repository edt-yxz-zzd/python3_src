see:
    "def - 2.1. infinite implicit graph.txt"

logical dfs
    # iterative deepening widening bdfs??
    # control be max_depth, max_width(max_fanout)?

    * dfs for finite graph
        # sources neednot cover whole graph
        #   so we can dfs partial graph
        #
        * explict
            # bgraph case is too complex
            # if tree then using implict version
            #
            * xgraph
                with keywords
                    sources :: [Vertex]
                xgraph methods:
                    .vertex_eq
                    .get_vertex_dict_ops
                    .get_vertex_set_ops
                    ...
                IN OUT???
                CASE???

                Explict_DFSColor2 = White | Black
                Explict_DFSColor3 = White | Black | Red

                # 5 Explict_DFSCase__Color2
                Explict_DFSCase__Color2
                    = (RootVertex|TreeEdge, Enter|Exit)
                    | (BackOrForwardOrCrossEdge, EnterExit)
                # 6 Explict_DFSCase__Color3
                Explict_DFSCase__Color3
                    = (RootVertex|TreeEdge, Enter|Exit)
                    | (BackEdge|ForwardOrCrossEdge, EnterExit)
                    #
                    # LoopEdge <: BackEdge
                    # ForwardEdge,CrossEdge can be distinguished by
                    #   (preordering :: Map Vertex UInt)


                # g = graph{.is_finite=True
                #   , .is_directed=??
                #   , .is_parented=??
                #   , .is_local_outgo_hedges_linear_ordered=??
                #   , .is_local_outgo_hedges_circlic_ordered=??
                #   , .vertex_eq
                #   , .outgo_vtx2unstable_iter_hedges
                #   , .hedge2another_vtx
                #   }
                # g -> Either sources unstable_iter_vertices
                #   -> color_2or3 -> init_vtx2color
                #       # all(init_vtx2color.get(vtx, White) == White
                #       #       for vtx in g.unstable_iter_vertices())
                #   -> Either # is_direced?
                #   (Maybe (hedge_eq, outgo_hedge2next_outgo_hedge))
                #   (Either &ancestor_hedges get_may_parent
                #   ,Maybe (get_may_first_outgo_hedge, outgo_hedge2may_next_outgo_hedge)
                #   )
                #   -> Iter (case, vtx)



        * implict
            # neednot color
            #
            # 4 Implict_DFSCase
            # Implict_DFSCase = (RootVertex|ChildVertex, Enter|Exit)
            #
            * sourced finite uforest with vertex_eq
                requires:
                    .vertex_eq

                # g = graph{.is_finite=True
                #   , .is_undirected=True
                #   , .is_forest=True
                #   , .is_local_outgo_hedges_circlic_ordered=??
                #   , .vertex_eq
                #   , .outgo_vtx2unstable_iter_hedges
                #   , .hedge2another_vtx
                #   }
                # g -> sources
                #   -> &ancestor_hedges
                #   -> Maybe (hedge_eq, outgo_hedge2next_outgo_hedge)
                #   -> Iter (case, vtx)
                #
                # (g<-FiniteUForest) -> [Vertex]
                #   -> INOUT Stack<HEdge>
                #   -> Maybe (g->HEdge->HEdge->Bool, g->HEdge->HEdge)
                #   -> Iter (Implict_DFSCase, Vertex)

            * sourced finite DAG_as_compact_forest
                with keywords:
                    is_parented     :: Bool
                    get_may_parent  :: Maybe (() -> Maybe Vertex)

                # g = graph{.is_finite=True
                #   , .is_DAG=True
                #   , .is_parented=??
                #   , .is_local_outgo_hedges_linear_ordered=??
                #   , .outgo_vtx2unstable_iter_hedges
                #   , .hedge2another_vtx
                #   }
                # g -> sources
                #   -> Either &ancestor_hedges get_may_parent
                #   -> Maybe (get_may_first_outgo_hedge, outgo_hedge2may_next_outgo_hedge)
                #   -> Iter (case, vtx)
                #
                # (g<-FiniteDAG) -> [Vertex]
                #   -> Either (INOUT Stack<HEdge>) (g->Vertex->Maybe Vertex)
                #   -> Maybe (g->Maybe HEdge, g->HEdge->Maybe HEdge)
                #   -> Iter (Implict_DFSCase, Vertex)

    * iterative deepening dfs for finite fanout infinite graph
        * implict
            * finite sourced finite fanout infinite uforest with vertex_eq
                requires:
                    .vertex_eq
            * finite sourced finite fanout infinite DAG_as_compact_forest


