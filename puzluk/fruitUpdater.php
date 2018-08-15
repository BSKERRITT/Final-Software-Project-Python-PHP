<?php
	session_start();
	/*
	// Retrieving the session and saving to a variable.
	if (isset($_SESSION["AvatarSession"])){
		
		// Counts the amount of times a page has been refreshed.
		if (empty($_SESSION['count'])) {
		   $_SESSION['count'] = 1;
		} else {
		   $_SESSION['count']++;
		}
		
		$sessionID = session_id();
		echo $sessionID;
		
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
	
		// Variables for the fruit column in users table
		$fruitvalue = isset($_POST["fruitValuePost"]);
		echo $fruitvalue;
		//$fruitvalue = 8;
		
		if (isset($fruitvalue) && !empty($fruitvalue)){
	
			//Accessing the logged in avatar session and updating the database row of the logged in user.	
			$sqlUpdate = "UPDATE users SET game1_fruit_selected = '".$fruitvalue."' WHERE avatar = '".$_SESSION["AvatarSession"]."'"; // Will need to update the individual game_fruit_selected per game.
			$result = mysqli_query($conn, $sqlUpdate);
			
			if($result){
				echo "Record updated successfully: " . $fruitvalue . " " . $_SESSION['count'] . " " . $_SESSION["AvatarSession"];
			} else {
				echo "Error updating record: " . mysqli_error($conn);
			}
		}
	}
	// remove all session variables
	session_unset(); 

	// destroy the session 
	session_destroy();
	*/
	
	
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
	
	// Variables for the fruit column in users table
	$fruitvalue = $_POST["fruitValuePost"];
	//$fruitvalue = 5;
	
	if(isset($_SESSION["Avatar"])){
		if (isset($fruitvalue) && !empty($fruitvalue)){
			//Accessing the logged in avatar session and updating the database row of the logged in user.	
			$sqlUpdate = "UPDATE users SET game1_fruit_selected = '".$fruitvalue."' WHERE avatar = '".$_SESSION["Avatar"]."'"; // Will need to update the individual game_fruit_selected per game.
			$result = mysqli_query($conn, $sqlUpdate);
			
			if($result){
				echo "Record updated successfully: " . $fruitvalue;
			} else {
				echo "Error updating record: " . mysqli_error($conn);
			}
		}
	}
	session_destroy();
?>