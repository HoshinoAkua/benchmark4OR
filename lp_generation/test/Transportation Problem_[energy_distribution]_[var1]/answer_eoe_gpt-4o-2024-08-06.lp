\ Model energy_distribution
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  2703.17984771664 transport(0,0) + 31267.40842780708 transport(0,1)
   + 67852.09073045873 transport(0,2) + 95839.65870408621 transport(0,3)
   + 39746.99857133054 transport(0,4) + 71609.75429180113 transport(0,5)
   + 7726.088617449687 transport(0,6) + 69180.41334648077 transport(0,7)
   + 62831.63668374006 transport(0,8) + 10307.57450894292 transport(1,0)
   + 77271.86541656 transport(1,1) + 85139.10136212267 transport(1,2)
   + 60089.69076026892 transport(1,3) + 12265.41126588856 transport(1,4)
   + 98434.91361522207 transport(1,5) + 78361.08998516756 transport(1,6)
   + 34854.72018216531 transport(1,7) + 42959.55735309607 transport(1,8)
   + 37169.11775947831 transport(2,0) + 50724.77824622464 transport(2,1)
   + 34198.30877316415 transport(2,2) + 84994.77256134103 transport(2,3)
   + 82320.04051485477 transport(2,4) + 10673.96071828817 transport(2,5)
   + 96140.83770771378 transport(2,6) + 63642.28341580551 transport(2,7)
   + 82940.95725304085 transport(2,8) + 70802.68963246948 transport(3,0)
   + 43679.76187058393 transport(3,1) + 73439.23669274448 transport(3,2)
   + 96621.11421635312 transport(3,3) + 27108.33033263469 transport(3,4)
   + 80864.24981237824 transport(3,5) + 53875.54773609713 transport(3,6)
   + 48420.66714143351 transport(3,7) + 43625.85612966713 transport(3,8)
   + 73183.10984698043 transport(4,0) + 26988.93559016992 transport(4,1)
   + 85204.66781867659 transport(4,2) + 83111.67508731275 transport(4,3)
   + 8806.048532497271 transport(4,4) + 88247.41653613621 transport(4,5)
   + 24559.61851139458 transport(4,6) + 46576.84425420503 transport(4,7)
   + 61100.44429296948 transport(4,8)
Subject To
 supply_0: transport(0,0) + transport(0,1) + transport(0,2)
   + transport(0,3) + transport(0,4) + transport(0,5) + transport(0,6)
   + transport(0,7) + transport(0,8) <= 153229.9634390056
 supply_1: transport(1,0) + transport(1,1) + transport(1,2)
   + transport(1,3) + transport(1,4) + transport(1,5) + transport(1,6)
   + transport(1,7) + transport(1,8) <= 127094.753899332
 supply_2: transport(2,0) + transport(2,1) + transport(2,2)
   + transport(2,3) + transport(2,4) + transport(2,5) + transport(2,6)
   + transport(2,7) + transport(2,8) <= 669789.3857752908
 supply_3: transport(3,0) + transport(3,1) + transport(3,2)
   + transport(3,3) + transport(3,4) + transport(3,5) + transport(3,6)
   + transport(3,7) + transport(3,8) <= 564405.6123480891
 supply_4: transport(4,0) + transport(4,1) + transport(4,2)
   + transport(4,3) + transport(4,4) + transport(4,5) + transport(4,6)
   + transport(4,7) + transport(4,8) <= 218746.5763655971
 demand_0: transport(0,0) + transport(1,0) + transport(2,0)
   + transport(3,0) + transport(4,0) = 699765.5062749047
 demand_1: transport(0,1) + transport(1,1) + transport(2,1)
   + transport(3,1) + transport(4,1) = 767131.2002578846
 demand_2: transport(0,2) + transport(1,2) + transport(2,2)
   + transport(3,2) + transport(4,2) = 168621.3542244345
 demand_3: transport(0,3) + transport(1,3) + transport(2,3)
   + transport(3,3) + transport(4,3) = 607640.2463970408
 demand_4: transport(0,4) + transport(1,4) + transport(2,4)
   + transport(3,4) + transport(4,4) = 748177.7263033305
 demand_5: transport(0,5) + transport(1,5) + transport(2,5)
   + transport(3,5) + transport(4,5) = 115418.3385075188
 demand_6: transport(0,6) + transport(1,6) + transport(2,6)
   + transport(3,6) + transport(4,6) = 819481.8731367739
 demand_7: transport(0,7) + transport(1,7) + transport(2,7)
   + transport(3,7) + transport(4,7) = 964756.0522610536
 demand_8: transport(0,8) + transport(1,8) + transport(2,8)
   + transport(3,8) + transport(4,8) = 108990.650907949
Bounds
End
