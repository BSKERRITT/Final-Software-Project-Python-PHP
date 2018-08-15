<?php
	session_start();
	session_regenerate_id();
	
	// Variables for server connection
	$servername = "localhost";
	$server_username = "root";
	$server_password = "";
	$dbName = "puzluk_db";
	
	// Variables for the users
	$name = $_POST["namePost"];
	$surname = $_POST["surnamePost"];
	$avatar = $_POST["avatarPost"];
	$games_played = "0";
	$lives = "10";
	$points = "0";
	$game1_fruit_selected = "0";
	$game1_object_identified = "0";
	
	//Make connection
	
	$conn = new mysqli($servername, $server_username, $server_password, $dbName);
	
	//Check connection
	
	if(!$conn){
		die("Connection Failed. " . mysqli_connect_error());
	}
	
	$sql = "INSERT INTO users (name, surname, avatar, games_played, lives, points,
			game1_fruit_selected, game1_object_identified)
			VALUES ('".$name."','".$surname."','".$avatar."','".$games_played."',
				'".$lives."','".$points."','".$game1_fruit_selected."',
				'".$game1_object_identified."')";
			
	$result = mysqli_query($conn, $sql);
	
	//Storing the avatar field as a user session.
	$_SESSION["AvatarSession"] = $avatar;
	//print_r($_SESSION["AvatarSession"]);
	
	if(!$result){
		echo "There was an error";
	}else{
		echo "New User Created. Everything OK";
	}
?>