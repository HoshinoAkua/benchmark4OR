\ Model energy_distribution
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  34.64002291936535 transport(0,0) + 12.26632436362423 transport(0,1)
   + 51.2123883461642 transport(0,2) + 81.52639078119903 transport(0,3)
   + 54.96656062268053 transport(0,4) + 74.66007626412917 transport(0,5)
   + 94.98443790109887 transport(0,6) + 92.49691308431818 transport(1,0)
   + 74.38758930717097 transport(1,1) + 12.42963331189255 transport(1,2)
   + 19.84335036069572 transport(1,3) + 19.10524845212558 transport(1,4)
   + 87.19849053001684 transport(1,5) + 74.63273430215645 transport(1,6)
   + 20.98332198138624 transport(2,0) + 95.2841699533426 transport(2,1)
   + 47.04034344677346 transport(2,2) + 58.78445236078079 transport(2,3)
   + 86.27096693610085 transport(2,4) + 12.401009879676 transport(2,5)
   + 80.43900018988231 transport(2,6) + 41.91336602810934 transport(3,0)
   + 11.55380147042434 transport(3,1) + 9.016159716497782 transport(3,2)
   + 69.47517120102272 transport(3,3) + 19.80633026254219 transport(3,4)
   + 82.02652637072481 transport(3,5) + 53.89932301421737 transport(3,6)
   + 43.86304066586607 transport(4,0) + 40.90282580160687 transport(4,1)
   + 27.19225432248819 transport(4,2) + 8.489810862379937 transport(4,3)
   + 90.67192337000752 transport(4,4) + 50.57915804226139 transport(4,5)
   + 43.98852163557839 transport(4,6) + 18.15179357726117 transport(5,0)
   + 72.78459788694411 transport(5,1) + 24.23787618321185 transport(5,2)
   + 16.55962332632962 transport(5,3) + 90.82766135335963 transport(5,4)
   + 65.31465436456982 transport(5,5) + 38.87950183786524 transport(5,6)
   + 38.91655505751368 transport(6,0) + 32.76013041270892 transport(6,1)
   + 62.06348938674278 transport(6,2) + 47.62924652197314 transport(6,3)
   + 7.050475537521193 transport(6,4) + 19.64861248667255 transport(6,5)
   + 5.116688660032328 transport(6,6) + 29.24547920579277 transport(7,0)
   + 55.12338713819032 transport(7,1) + 30.19582962020092 transport(7,2)
   + 22.2853671334025 transport(7,3) + 69.30145496892129 transport(7,4)
   + 24.08399754175175 transport(7,5) + 87.30124259997027 transport(7,6)
   + 4.987773242943398 transport(8,0) + 39.90323144121457 transport(8,1)
   + 33.68714887235362 transport(8,2) + 47.92448930291944 transport(8,3)
   + 25.67309916903438 transport(8,4) + 22.0634240622454 transport(8,5)
   + 14.14309977433571 transport(8,6) + 7.985015118680673 transport(9,0)
   + 85.38195915523315 transport(9,1) + 62.50401931323119 transport(9,2)
   + 74.04220926550171 transport(9,3) + 62.63586690841232 transport(9,4)
   + 84.10283593689022 transport(9,5) + 79.06642217880447 transport(9,6)
Subject To
 supply_0: transport(0,0) + transport(0,1) + transport(0,2)
   + transport(0,3) + transport(0,4) + transport(0,5) + transport(0,6)
   <= 1834.558256221539
 supply_1: transport(1,0) + transport(1,1) + transport(1,2)
   + transport(1,3) + transport(1,4) + transport(1,5) + transport(1,6)
   <= 6101.842795834198
 supply_2: transport(2,0) + transport(2,1) + transport(2,2)
   + transport(2,3) + transport(2,4) + transport(2,5) + transport(2,6)
   <= 9869.470708362609
 supply_3: transport(3,0) + transport(3,1) + transport(3,2)
   + transport(3,3) + transport(3,4) + transport(3,5) + transport(3,6)
   <= 1479.008245966232
 supply_4: transport(4,0) + transport(4,1) + transport(4,2)
   + transport(4,3) + transport(4,4) + transport(4,5) + transport(4,6)
   <= 3301.42721314722
 supply_5: transport(5,0) + transport(5,1) + transport(5,2)
   + transport(5,3) + transport(5,4) + transport(5,5) + transport(5,6)
   <= 3156.827887932197
 supply_6: transport(6,0) + transport(6,1) + transport(6,2)
   + transport(6,3) + transport(6,4) + transport(6,5) + transport(6,6)
   <= 7049.832439627639
 supply_7: transport(7,0) + transport(7,1) + transport(7,2)
   + transport(7,3) + transport(7,4) + transport(7,5) + transport(7,6)
   <= 1359.009863430821
 supply_8: transport(8,0) + transport(8,1) + transport(8,2)
   + transport(8,3) + transport(8,4) + transport(8,5) + transport(8,6)
   <= 2234.085039311703
 supply_9: transport(9,0) + transport(9,1) + transport(9,2)
   + transport(9,3) + transport(9,4) + transport(9,5) + transport(9,6)
   <= 9943.855538674761
 demand_0: transport(0,0) + transport(1,0) + transport(2,0)
   + transport(3,0) + transport(4,0) + transport(5,0) + transport(6,0)
   + transport(7,0) + transport(8,0) + transport(9,0) = 5560.422864466414
 demand_1: transport(0,1) + transport(1,1) + transport(2,1)
   + transport(3,1) + transport(4,1) + transport(5,1) + transport(6,1)
   + transport(7,1) + transport(8,1) + transport(9,1) = 3848.840735542145
 demand_2: transport(0,2) + transport(1,2) + transport(2,2)
   + transport(3,2) + transport(4,2) + transport(5,2) + transport(6,2)
   + transport(7,2) + transport(8,2) + transport(9,2) = 1283.500475372164
 demand_3: transport(0,3) + transport(1,3) + transport(2,3)
   + transport(3,3) + transport(4,3) + transport(5,3) + transport(6,3)
   + transport(7,3) + transport(8,3) + transport(9,3) = 6714.664911667872
 demand_4: transport(0,4) + transport(1,4) + transport(2,4)
   + transport(3,4) + transport(4,4) + transport(5,4) + transport(6,4)
   + transport(7,4) + transport(8,4) + transport(9,4) = 8267.410895061494
 demand_5: transport(0,5) + transport(1,5) + transport(2,5)
   + transport(3,5) + transport(4,5) + transport(5,5) + transport(6,5)
   + transport(7,5) + transport(8,5) + transport(9,5) = 1945.046726216604
 demand_6: transport(0,6) + transport(1,6) + transport(2,6)
   + transport(3,6) + transport(4,6) + transport(5,6) + transport(6,6)
   + transport(7,6) + transport(8,6) + transport(9,6) = 8900.080774352609
Bounds
End
