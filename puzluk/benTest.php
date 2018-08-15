<?php

	// Variables for server connection
	$servername = "localhost";
	$server_username = "root";
	$server_password = "";
	$dbName = "puzluk_db";
	
	// Variables for the users
	$name = $_POST["namePost"];
	$surname = $_POST["surnamePost"];
	$avatar = $_POST["avatarPost"];
	//$name = "Ben";
	//$surname = "Skerritt";
	//$avatar = "Dog";
	$games_played = "0";
	$lives = "10";
	$points = "0";
	$fruitvalue = $_POST["fruitValuePost"];
	$game1_object_identified = "0";
	
	//Make connection
	
	$conn = new mysqli($servername, $server_username, $server_password, $dbName);
	
	//Check connection
	
	if(!$conn){
		die("Connection Failed. " . mysqli_connect_error());
	}
	
	$sql = "UPDATE users SET game1_fruit_selected = '".$fruitvalue."' WHERE avatar = '".$avatar."'"; // Will need to update the individual game_fruit_selected per game.
			$result = mysqli_query($conn, $sqlUpdate);
			
			if($result){
				echo "Record updated successfully: " . $fruitvalue;
			} else {
				echo "Error updating record: " . mysqli_error($conn);
			}
			
	$result = mysqli_query($conn, $sql);
	
	//print_r($_SESSION["AvatarSession"]);
	
	if(!$result){
		echo "There was an error";
	}else{
		echo "New User Created. Everything OK";
	}
?>