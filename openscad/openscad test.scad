path = "features/";
heads = ["alien-head", "moose-head", "orc-head"];
left = ["alien-left-arm",
    "alien-left-leg",
    "orc-left-arm",
   "orc-left-foot", "moose-left-back-foot", 
    "moose-left-front-foot"];
right = ["alien-right-arm",
    "alien-right-leg",
    "orc-right-arm",
    "orc-left-foot",
    "moose-right-back-foot",
    "moose-right-front-foot"];
torso = ["alien-torso",
    "moose-torso",
    "orc-torso"];

headSelected = floor(rands(0, 2.99, 1)[0]);
torsoSelected = floor(rands(0, 2.99, 1)[0]);
armSelected = floor(rands(0, 5.99, 1)[0]);
echo(str(headSelected, torsoSelected, armSelected));

// torso first
scale([5,5,5]){
    if(torsoSelected == 0){
        translate([0,0,-2]){
            import(str(path,torso[torsoSelected], ".stl"));
        }
    }else{
        translate([0, 0, 3]){
            import(str(path,torso[torsoSelected], ".stl"));
        }
    }
}

// then the head
scale([5,5,5]){
    translate([0, -1, 5]){
        import(str(path,heads[headSelected], ".stl"));
    }
}

// now the limbs
if(torsoSelected == 1){
    // left side
    for(a = [0:1]){
        if(armSelected == 0 || armSelected == 1){
            translate([3, (a*-4)+2, 0]){
                import(str(path, left[armSelected], ".stl"));
            }
        }else{
                scale([5,5,5]){
                    translate([3, (a*-4)+2, 0]){
                        import(str(path, left[armSelected], ".stl"));
                    }
                }
            }
        }
    
    for(a = [0:1]){
        if(armSelected == 0 || armSelected == 1){
            translate([-3, (a*-4)+2, 0]){
                import(str(path, right[armSelected], ".stl"));
            }
        }else{
            scale([5,5,5]){
                translate([-3, (a*-4)+2, 0]){
                    import(str(path, right[armSelected], ".stl"));
                }
            }
        }
    }
    // right side
}
else{
    // legs
    scale([5,5,5]){
        translate([-3, 0, -2]){
            import(str(path, right[armSelected], ".stl"));
        }
        translate([3, 0, -2]){
            import(str(path, left[armSelected], ".stl"));
        }
    }
    // arms
    scale([5,5,5]){
        translate([-5, 0, 5]){
            import(str(path, right[armSelected], ".stl" ));
        }
        translate([5, 0, 5]){
            import(str(path, right[armSelected], ".stl" ));
        }
    }
}