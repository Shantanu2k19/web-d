<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
    </head>

    <body>
        <form action="site4.php" method="post">
            type a character (a or b) : <input type="text" name="charr">
        <input type="submit">
        <br><br>

        <?php
            $isMale = true;
            $istall = false;
            if($isMale && $istall){  //both true 
                echo "you're tall male  <br><br>";
            }
            elseif($isMale && !$istall){
                echo "you are a short male  <br><br>";
            }
            else{
                echo "you are not male  <br><br>";
            }

            //switch statements 
            $character = $_POST["charr"];
            switch($character){
                case "a": echo "you entered a";
                break;
                case "b": echo "you entered b";
                break;
                default : echo "characted a or b only";
            }


            //While statement 
            $index = 0;
            while( $index <=5){
                 echo "<br><br> -> index value : $index";
                $index++;
            }

            //for loop
            for( $i=0; $i<5 ;$i++){
                echo "<br><br> => for loop i value : $i";
            }

        ?>
    </body>
</html>