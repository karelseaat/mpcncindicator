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


translate([0,0,50])
difference()
{
        cylinder(10, 50, 50);
cylinder(10, 45,45);
}

difference()
{
    cylinder(50, 50, 50);
    cylinder(50, 30,30);
}