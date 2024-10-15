color("yellow")
translate([0,0,20])
difference()
{
intersection()
{
translate([0,0,55])
cylinder(20, 50, 50);
sphere(r=75, $fn=65);
}
translate([0,0,70])
cylinder(5,5,5);

cylinder(100,2,2);
}

color("red")
union()
{
translate([0,0,60])
difference()
{
    cylinder(5, 50, 50,$fn=65);
    cylinder(5, 45,45);
}


difference()
{
    cylinder(60, 50, 50,$fn=65);
    cylinder(60, 30,30);
}
}

color("blue")
translate([0,0,-50])
difference()
{
    cylinder(10, 30,30);
    cylinder(100,2,2);
    translate([28,0,0])
    cylinder(100,2,2);
}