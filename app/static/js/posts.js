$( document ).ready(() => {
	let likeButtons = $('[id^="like-"]');
	console.log(likeButtons);
	likeButtons.click(likePost);
});

const likePost = (e) => {
	let id = e.target.id.split("-")[1];
	$.ajax({
		url: `posts/like-post?post_id=${id}`,
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
