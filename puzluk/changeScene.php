<?php
	session_start();

	$servername = "localhost";
	$username = "root";
	$password = "";
	$dbName = "puzluk_db";
	
	//Make connection
	
	$conn = new mysqli($servername, $username, $password, $dbName);
	
	//Check connection
	
	if(!$conn){
		die("Connection Failed. " . mysqli_connect_error());
	}
	
	// Retrieving the session and saving to a variable.
	if (isset($_SESSION["AvatarSession"])){
		print_r($_SESSION["AvatarSession"]);

		//Accessing the logged in avatar session and selecting the database row of the logged in user.
		$sql = "SELECT game1_object_identified FROM users WHERE avatar = '".$_SESSION["AvatarSession"]."'"; // Will need to select the individual game_object_identified per game.
		$result = mysqli_query($conn, $sql);
		
		// Getting a result and confirming object has been successfully identified
		if(mysqli_num_rows($result) > 0){
			//Show data for each row
			while($row = mysqli_fetch_assoc($result)){
				if($row['game1_object_identified'] == 1){
					echo $row['game1_object_identified'];
				}else{
					echo "Wrong fruit, try again!";
				}
			}
		}else{
			echo "Game already successfully completed!";
		}
	}
?>