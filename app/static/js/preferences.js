"usestrict";
document.addEventListener("DOMContentLoaded", () => {
	let liElems = document.querySelectorAll("li");
	for (li of liElems) {
		li.classList.add("list-group-item");
	}
});
