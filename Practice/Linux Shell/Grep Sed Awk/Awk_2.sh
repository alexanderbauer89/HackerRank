awk '{if ($2 > 49 && $3 > 49 && $4 > 49) print $1,": Pass"; else print $1,": Fail";}'
