//color("yellow")
//translate([0,0,20])
//difference()
//{
//    intersection()
//    {
//        translate([0,0,70])
//        cylinder(10, 25, 25);
//        sphere(r=75, $fn=65);
//    }
//    translate([0,0,73])
//    cylinder(2,5,5);
//
//    cylinder(100,2,2);
//}
//
//color("red")
//union()
//{
//    translate([0,0,60])
//    difference()
//    {
//        cylinder(5, 25, 25,$fn=65);
//        cylinder(5, 23,23);
//    }
//
//    difference()
//    {
//        cylinder(60, 25, 25,$fn=65);
//        cylinder(60, 20,20);
//    }
//}
//
color("blue")
translate([0,0,-50])
difference()
{   
    union()
    {
        translate([0,0,5])
        cylinder(5, 15, 15);
        cylinder(5, 20,20);
    }
    cylinder(100,2,2);
    translate([17,0,0])
    cylinder(100,4,4);
}