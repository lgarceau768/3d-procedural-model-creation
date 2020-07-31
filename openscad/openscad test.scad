path = "features/";
heads = ["alien-head", "moose-head", "orc-head"];
left = ["alien-left-arm",
    "alien-left-foot",
    "orc-left-arm",
   "orc-left-foot", "moose-left-back-foot", 
    "moose-left-front-foot"];
right = ["alien-right-arm",
    "alien-right-foot",
    "orc-right-arm",
    "orc-left-foot",
    "moose-right-back-foot",
    "moose-right-front-foot"];
torso = ["alien-torso",
    "moose-torso",
    "orc-torso"];

headSelected = ceil(rands(0, 2, 1)[0]);
torsoSelected = ceil(rands(0, 2, 1)[0]);
armSelected = ceil(rands(0, 5, 1)[0]);
echo(str(headSelected, torsoSelected, armSelected));

// torso first
scale([5,5,5]){
    import(str(path,torso[torsoSelected], ".stl"));
}

// then the head
scale([5,5,5]){
    translate([0, -2, 3]){
        import(str(path,heads[headSelected], ".stl"));
    }
}

// now the limbs
if(torsoSelected == 1){
    // left side
    for(a = [0:1]){
        scale([5,5,5]){
            translate([5, (a*-4)+2, 0]){
                import(str(path, left[armSelected], ".stl"));
            }
        }
    }
    for(a = [0:1]){
        scale([5,5,5]){
            translate([-5, (a*-4)+2, 0]){
                import(str(path, right[armSelected], ".stl"));
            }
        }
    }
    // right side
}
else{
    // legs
    scale([5,5,5]){
        translate([-5, 0, -2]){
            import(str(path, right[armSelected], ".stl"));
        }
        translate([5, 0, -2]){
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