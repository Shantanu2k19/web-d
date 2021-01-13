<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
    </head>

    <body>
        <form action = "site3.php" method="post">
            Enter your name : <input type="text" name="student">
            <input type="submit">
        </form>

        <?php 
            // 'key' mapped to a 'value' : associative array 
            $grades = array("jim"=>"A+", "pam"=>"A-", "kim"=>"D+");
            echo $grades["jim"]."<br>";   //grade jim got 
            $grades["jim"]="B+";
            echo count($grades)." total no of students <br>";

            echo $grades[$_POST["student"]]." scored by ".$_POST["student"];


            //FUNCTION 
            function sayHi($name, $age){
                echo "<br><br>Hello $name aged $age!";
                return $age*$age;
            }

            //calling the function with argument as name of student from post and the age 18
            //it returns 18square 
            $ageSQ = sayHi($_POST["student"], 18);
            echo "<br>your age square is : $ageSQ";
            
        ?>
    </body>
</html>