awk '{ 
        if (($2 + $3 + $4)/3 > 79)      print $1,$2,$3,$4" : A"; 
        else if (($2 + $3 + $4)/3 > 59) print $1,$2,$3,$4" : B"; 
        else if (($2 + $3 + $4)/3 > 49) print $1,$2,$3,$4" : C";
        else                            print $1,$2,$3,$4" : FAIL"
    }'
