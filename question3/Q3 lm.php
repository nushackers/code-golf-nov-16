function($x){$d="";while($x-1){$x=($x%2)?(int)pow(sqrt($x),3):(int)sqrt($x);$d.=",".$x;return substr($d,1);}}