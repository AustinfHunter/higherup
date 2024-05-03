$( document ).ready(() => {
	let likeButtons = $('[id^="like-"]');
	likeButtons.click(likePost);

	let deletePostButtons = $('[id^="delete-post-"]');
	deletePostButtons.click(deletePost);
	
	let deleteCommentButtons = $('[id^="delete-comment-"]');
	deleteCommentButtons.click(deleteComment);
});

const likePost = (e) => {
	let id = e.target.id.split("-")[1];
	$.ajax({
		url: `/posts/like-post?post_id=${id}`,
		method: "POST",
		})
		.done((data) => {
			console.log(`id: ${id}`);
			let like = $(`#like-${id}`);
			console.log(data.likeUpdate);
			console.log(like);
			if (data.likeUpdate == "added") {
				like.removeClass("bi-arrow-up-circle");
				like.addClass("bi-arrow-up-circle-fill");
				let likeCountElem = $(`#like-count-${id}`);
				let count = parseInt(likeCountElem.html()) + 1;
				likeCountElem.html(count);
			} else {
				like.removeClass("bi-arrow-up-circle-fill");
				like.addClass("bi-arrow-up-circle");
				let likeCountElem = $(`#like-count-${id}`);
				let count = parseInt(likeCountElem.html()) - 1;
				likeCountElem.html(count);
			}
	})
}

const deletePost = (e) => {
	if (confirm("Are you sure you want to delete this post?")) {
		let id = e.target.id.split("-")[2];
		$.ajax({
			url: `/posts/deletepost/${id}`,
			method: "DELETE",
			})
			.done(() => {
				location.reload();
		})
	}
}

const deleteComment = (e) => {
	if (confirm("Are you sure you want to delete this comment?")) {
		let id = e.target.id.split("-")[2];
		$.ajax({
			url: `/posts/deletecomment/${id}`,
			method: "DELETE",
			})
			.done(() => {
				location.reload();
		})
	}
}
