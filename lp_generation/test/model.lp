\ Model Water Resource Management
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  2 x00 + 4 x01 + x02 + 5 x03 + 7 x04 + 9 x10 + 9.1 x11
   + 10 x12 + 9.2 x13 + 10.1 x14 + 10.2 x20 + 1.1x21 + 9.3 x22
   + 3 x23 + 1.4x24 + 5.1 x30 + 7.1 x31 + 10.3 x32 + 7.4 x33
   + 6.1 x34 + 4.1 x40 + 6 x41 + 7.2 x42 + 1.6x43 + 4.2 x44
Subject To
 supply_0: x00 + x01 + x02 + x03 + x04 <= 68
 supply_1: x10 + x11 + x12 + x13 + x14 <= 92
 supply_2: x20 + x21 + x22 + x23 + x24 <= 50
 supply_3: x30 + x31 + x32 + x33 + x34 <= 97.1
 supply_4: x40 + x41 + x42 + x43 + x44 <= 97
 demand_0: x00 + x10 + x20 + x30 + x40 >= 39
 demand_1: x01 + x11 + x21 + x31 + x41 >= 35
 demand_2: x02 + x12 + x22 + x32 + x42 >= 32
 demand_3: x03 + x13 + x23 + x33 + x43 >= 58
 demand_4: x04 + x14 + x24 + x34 + x44 >= 46
Bounds
End
