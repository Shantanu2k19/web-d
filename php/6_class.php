<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
    </head>

    <body>
        <?php 
            //class created 
            class Book{
                var $author;
                var $pages;
                var $title;

                private $rating;

                function __construct($Author, $Pages, $Title, $Rating){
                    echo "class is created, constructer is called<br><br>";
                    $this->title=$Title;
                    $this->author=$Author;
                    $this->pages=$Pages;
                    $this->setRating($Rating); //for setter
                }

                //object function
                function pagesLessThan100(){
                    if($this->pages >=100)  return "false";
                    return "true";
                }

                //getter and setter used to assign and access values of private attributes
                //Getter 
                function getRating(){
                    return $this->rating;
                }

                //Setter
                function setRating($Rating){
                    if($Rating == "A" || $Rating=="B" || $Rating =="C")
                        $this->rating = $Rating;

                    else
                        echo "not valid rating<br>";
                }

            }
            
            //object created (instance of class)
            $book1 = new Book("elon",420,"spaceX","A");
            
            $book1->title = "Tesla <br>";
            echo $book1->title;  

            // $book1->rating = "A";  can'nt do, rating is private
            // echo $book1->rating;

            $book1->setRating("As");

            echo $book1->getRating();


            echo "<br>".$book1->pagesLessThan100()."<br>";
        ?>
    </body>

</html>