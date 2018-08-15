<?php
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
	
	$sql = "SELECT ID, name, surname, games_played, object_identified FROM users";
	$result = mysqli_query($conn, $sql);
	
	if(mysqli_num_rows($result) > 0){
		//Show data for each row
		while($row = mysqli_fetch_assoc($result)){
			echo "ID:".$row['ID'] . "|Name:" .$row['name'] . "|Surname:" .$row['surname'] . "|Games Played:" .$row['games_played'] . "|Object Identified:" .$row['object_identified'] . ";";
		}
	}
?>