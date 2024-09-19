\ Model water_resource_management
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  5.309908091510887 transport(0,0) + 39.3012508312084 transport(0,1)
   + 37.95693632298242 transport(0,2) + 74.98434256470189 transport(0,3)
   + 36.35229377495855 transport(0,4) + 7.688396216447994 transport(0,5)
   + 24.87146651417882 transport(1,0) + 66.05333560107231 transport(1,1)
   + 11.26272288246926 transport(1,2) + 58.60842883425587 transport(1,3)
   + 75.91121371775375 transport(1,4) + 14.20754939607704 transport(1,5)
   + 35.87760556530476 transport(2,0) + 34.51617855979038 transport(2,1)
   + 64.63676600406933 transport(2,2) + 83.20798201959667 transport(2,3)
   + 68.78357407448937 transport(2,4) + 98.10109939309608 transport(2,5)
   + 48.37458599017448 transport(3,0) + 19.04552184297345 transport(3,1)
   + 14.35040553843195 transport(3,2) + 71.88846070202327 transport(3,3)
   + 94.4169099205008 transport(3,4) + 4.661395229777796 transport(3,5)
   + 20.95750829083339 transport(4,0) + 79.31981210967535 transport(4,1)
   + 88.6932481761924 transport(4,2) + 32.2439861849228 transport(4,3)
   + 31.69751241075229 transport(4,4) + 40.42418151291569 transport(4,5)
   + 81.72520198494225 transport(5,0) + 47.8665770000075 transport(5,1)
   + 4.625456382153926 transport(5,2) + 65.04314938127428 transport(5,3)
   + 29.32497865960332 transport(5,4) + 86.35171451645579 transport(5,5)
   + 5.732599390402647 transport(6,0) + 65.91740538821028 transport(6,1)
   + 28.04844400527347 transport(6,2) + 80.13489874030573 transport(6,3)
   + 44.2581869293687 transport(6,4) + 40.60215568980173 transport(6,5)
   + 44.53392673707836 transport(7,0) + 95.69139306454235 transport(7,1)
   + 34.5646262124079 transport(7,2) + 19.49490454140394 transport(7,3)
   + 69.51478062014888 transport(7,4) + 37.36734576900852 transport(7,5)
   + 79.93179715728989 transport(8,0) + 27.40534888441608 transport(8,1)
   + 9.178539156772569 transport(8,2) + 43.02546647052297 transport(8,3)
   + 43.63010804834124 transport(8,4) + 99.51471831956347 transport(8,5)
Subject To
 ReservoirCapacity_0: transport(0,0) + transport(0,1) + transport(0,2)
   + transport(0,3) + transport(0,4) + transport(0,5) <= 7466.898950131174
 ReservoirCapacity_1: transport(1,0) + transport(1,1) + transport(1,2)
   + transport(1,3) + transport(1,4) + transport(1,5) <= 3621.447889977321
 ReservoirCapacity_2: transport(2,0) + transport(2,1) + transport(2,2)
   + transport(2,3) + transport(2,4) + transport(2,5) <= 1014.079023400591
 ReservoirCapacity_3: transport(3,0) + transport(3,1) + transport(3,2)
   + transport(3,3) + transport(3,4) + transport(3,5) <= 4175.344356634305
 ReservoirCapacity_4: transport(4,0) + transport(4,1) + transport(4,2)
   + transport(4,3) + transport(4,4) + transport(4,5) <= 6135.97344420186
 ReservoirCapacity_5: transport(5,0) + transport(5,1) + transport(5,2)
   + transport(5,3) + transport(5,4) + transport(5,5) <= 2685.825206185443
 ReservoirCapacity_6: transport(6,0) + transport(6,1) + transport(6,2)
   + transport(6,3) + transport(6,4) + transport(6,5) <= 7013.934126276713
 ReservoirCapacity_7: transport(7,0) + transport(7,1) + transport(7,2)
   + transport(7,3) + transport(7,4) + transport(7,5) <= 5711.361019103902
 ReservoirCapacity_8: transport(8,0) + transport(8,1) + transport(8,2)
   + transport(8,3) + transport(8,4) + transport(8,5) <= 4245.433819361879
 FieldRequirement_0: 0.9737589162655719 transport(0,0)
   + 0.9254103379819509 transport(1,0) + 0.9346633666021112 transport(2,0)
   + 0.9534410791643113 transport(3,0) + 0.9289720015204096 transport(4,0)
   + 0.9045479599308073 transport(5,0) + 0.9830803114052642 transport(6,0)
   + 0.9876677993222271 transport(7,0) + 0.9266365969913857 transport(8,0)
   >= 4790.316550934817
 FieldRequirement_1: 0.9635610222897751 transport(0,1)
   + 0.9750019705140678 transport(1,1) + 0.9508553546316177 transport(2,1)
   + 0.9438222582481903 transport(3,1) + 0.950564445755393 transport(4,1)
   + 0.98708532084183 transport(5,1) + 0.9776074402954326 transport(6,1)
   + 0.9732556755474659 transport(7,1) + 0.9706886617118652 transport(8,1)
   >= 2948.36881967615
 FieldRequirement_2: 0.9807661882996097 transport(0,2)
   + 0.9500482457009015 transport(1,2) + 0.9324477620556768 transport(2,2)
   + 0.9225091814164299 transport(3,2) + 0.9786392978127971 transport(4,2)
   + 0.9761905652946563 transport(5,2) + 0.9569745046211551 transport(6,2)
   + 0.9434029253212447 transport(7,2) + 0.9349310535512722 transport(8,2)
   >= 4038.855511303929
 FieldRequirement_3: 0.9604872085192596 transport(0,3)
   + 0.9497583306296769 transport(1,3) + 0.9187669954053208 transport(2,3)
   + 0.9756011946070862 transport(3,3) + 0.9687604157621683 transport(4,3)
   + 0.9495069688156685 transport(5,3) + 0.9617053102816606 transport(6,3)
   + 0.9077811744768132 transport(7,3) + 0.9275417423063286 transport(8,3)
   >= 2784.301649732022
 FieldRequirement_4: 0.9633924045593691 transport(0,4)
   + 0.9245867043860008 transport(1,4) + 0.9848377742115132 transport(2,4)
   + 0.9871973442818959 transport(3,4) + 0.9319353411870482 transport(4,4)
   + 0.956613194320491 transport(5,4) + 0.964917921033017 transport(6,4)
   + 0.9794015104058392 transport(7,4) + 0.9001234040840863 transport(8,4)
   >= 591.504378296746
 FieldRequirement_5: 0.9498675813210312 transport(0,5)
   + 0.9079553492238347 transport(1,5) + 0.9295934499995699 transport(2,5)
   + 0.9136197621026518 transport(3,5) + 0.9574064475710922 transport(4,5)
   + 0.9500454639741956 transport(5,5) + 0.9035531952961506 transport(6,5)
   + 0.9202531964821661 transport(7,5) + 0.9719839493107991 transport(8,5)
   >= 4429.99147337383
Bounds
End
