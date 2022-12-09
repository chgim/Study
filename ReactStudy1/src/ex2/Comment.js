import React from "react";

const styles={
    wrapper:{
        margin:8,
        padding:8,
        display:"flex",
        flexDirection:"row",
        border:"2px solid grey",
        borderRadius:16,
        backgroundColor:"LightYellow"
    },
    imageContainer:{},
    image:{
        width:50,
        height:50,
        borderRadius:25,
    },
    contentContainer:{
        marginLeft:8,
        display:"flex",
        flexDirection:"column",
        justifyContent:"center"
    },
    nameText:{
        color:"Brown",
        fontSize:16,
        fontWeight:"bold"
    },
    commentText:{
        color:"black",
        fontSize:16,
    },
};
function Comment(props) {
	return (
		<div style={styles.wrapper}>
			<div style={styles.imageContainer}>
				<img
					src="https://cdn.imweb.me/upload/S20211110a3d216dc49446/f7bfffacbb6de.png"
					style={styles.image}
				/>
			</div>
			<div style={styles.contentContainer}>
				<span style={styles.nameText}>{props.name}</span>
				<span style={styles.commentText}>{props.comment}</span>
			</div>
		</div>
	);
}

export default Comment;