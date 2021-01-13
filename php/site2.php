<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title></title>
    </head>

    <body>
        <!-- checkboxes -->
        <form action="site2.php" method="post">
            apple : <input type = "checkbox" name="fruits[]" value="apple"><br>
            orange : <input type = "checkbox" name="fruits[]" value="orange"><br>
            mango : <input type = "checkbox" name="fruits[]" value="mango"><br>
        <input type ="submit">

        <!-- PHP -->
        <br><br>
        <?php 
            //ARRAY 
            $friends = array("shan","pdf","R","GG");
            echo $friends."<br>";
            $friends[5]="zodiac";
            echo $friends[0]." is friends with : ".$friends[5]."<br>";
            echo count($friends)." in total <br><br><br>";

            //CHECK BOXES 
            $fal =$_POST["fruits"]; //array holding all fruits
            echo $fal[1];

        ?>
        
    </body>
</html>
