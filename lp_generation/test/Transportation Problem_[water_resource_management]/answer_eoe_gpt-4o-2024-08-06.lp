\ Model water_resource_management
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  99.37052871583691 transport(0,0) + 97.0527376638903 transport(0,1)
   + 62.91320535120456 transport(0,2) + 79.37977416249383 transport(0,3)
   + 19.71745371780671 transport(0,4) + 67.06493873053928 transport(0,5)
   + 52.45333699826677 transport(0,6) + 61.10282776116401 transport(0,7)
   + 63.65066815630868 transport(1,0) + 39.04978520789651 transport(1,1)
   + 68.2593862024401 transport(1,2) + 63.02540037917292 transport(1,3)
   + 47.32226799535299 transport(1,4) + 86.18269812202686 transport(1,5)
   + 28.6295860446965 transport(1,6) + 16.96657860173388 transport(1,7)
   + 78.057291667309 transport(2,0) + 85.36369527570275 transport(2,1)
   + 96.41457793764289 transport(2,2) + 82.4448559525954 transport(2,3)
   + 57.79922646727088 transport(2,4) + 7.697049966798375 transport(2,5)
   + 69.61368818572537 transport(2,6) + 5.05555661307578 transport(2,7)
   + 71.63982719892682 transport(3,0) + 79.51621311630832 transport(3,1)
   + 17.17725033257368 transport(3,2) + 24.153346310503 transport(3,3)
   + 1.606612937903344 transport(3,4) + 16.29174477629692 transport(3,5)
   + 79.01360758509824 transport(3,6) + 48.79088217397893 transport(3,7)
   + 16.58833814963537 transport(4,0) + 14.15991649392034 transport(4,1)
   + 76.45158020211208 transport(4,2) + 60.1819801916059 transport(4,3)
   + 16.55387732073306 transport(4,4) + 91.39541521947204 transport(4,5)
   + 91.67062597497451 transport(4,6) + 36.17573659690196 transport(4,7)
   + 14.18512549102984 transport(5,0) + 71.85397559638723 transport(5,1)
   + 60.23562695084146 transport(5,2) + 87.50188157922121 transport(5,3)
   + 5.684488933139572 transport(5,4) + 63.10258423306126 transport(5,5)
   + 11.68228142960034 transport(5,6) + 52.54877593164309 transport(5,7)
Subject To
 reservoir_capacity_0: transport(0,0) + transport(0,1) + transport(0,2)
   + transport(0,3) + transport(0,4) + transport(0,5) + transport(0,6)
   + transport(0,7) <= 3653.847515373628
 reservoir_capacity_1: transport(1,0) + transport(1,1) + transport(1,2)
   + transport(1,3) + transport(1,4) + transport(1,5) + transport(1,6)
   + transport(1,7) <= 5893.505671056924
 reservoir_capacity_2: transport(2,0) + transport(2,1) + transport(2,2)
   + transport(2,3) + transport(2,4) + transport(2,5) + transport(2,6)
   + transport(2,7) <= 5392.434480871502
 reservoir_capacity_3: transport(3,0) + transport(3,1) + transport(3,2)
   + transport(3,3) + transport(3,4) + transport(3,5) + transport(3,6)
   + transport(3,7) <= 8838.57899335125
 reservoir_capacity_4: transport(4,0) + transport(4,1) + transport(4,2)
   + transport(4,3) + transport(4,4) + transport(4,5) + transport(4,6)
   + transport(4,7) <= 3691.990485165113
 reservoir_capacity_5: transport(5,0) + transport(5,1) + transport(5,2)
   + transport(5,3) + transport(5,4) + transport(5,5) + transport(5,6)
   + transport(5,7) <= 4662.265532089258
 field_requirement_0: transport(0,0) + transport(1,0) + transport(2,0)
   + transport(3,0) + transport(4,0) + transport(5,0) = 1621.713196711289
 field_requirement_1: transport(0,1) + transport(1,1) + transport(2,1)
   + transport(3,1) + transport(4,1) + transport(5,1) = 2991.56453177947
 field_requirement_2: transport(0,2) + transport(1,2) + transport(2,2)
   + transport(3,2) + transport(4,2) + transport(5,2) = 1846.960048280212
 field_requirement_3: transport(0,3) + transport(1,3) + transport(2,3)
   + transport(3,3) + transport(4,3) + transport(5,3) = 1226.466327958623
 field_requirement_4: transport(0,4) + transport(1,4) + transport(2,4)
   + transport(3,4) + transport(4,4) + transport(5,4) = 2048.559454086912
 field_requirement_5: transport(0,5) + transport(1,5) + transport(2,5)
   + transport(3,5) + transport(4,5) + transport(5,5) = 2268.065690825379
 field_requirement_6: transport(0,6) + transport(1,6) + transport(2,6)
   + transport(3,6) + transport(4,6) + transport(5,6) = 2576.854287375548
 field_requirement_7: transport(0,7) + transport(1,7) + transport(2,7)
   + transport(3,7) + transport(4,7) + transport(5,7) = 2820.749364878786
Bounds
End
