const generateBtn = document.getElementById("generateBtn");
const ingredientsInput = document.getElementById("ingredients");
const resultDiv = document.getElementById("result");
const loadingDiv = document.getElementById("loading");

generateBtn.addEventListener("click", async () => {
	const ingredients = ingredientsInput.value;
	if (!ingredients) {
		alert("Please enter ingredients.");
		return;
	}

	resultDiv.innerHTML = "";
	loadingDiv.style.display = "block";

	const response = await fetch("/generate", {
		method: "POST",
		headers: {
			"Content-Type": "application/json",
		},
		body: JSON.stringify({
			ingredients: ingredients,
		}),
	});

	const data = await response.json();
	loadingDiv.style.display = "none";
	resultDiv.innerHTML = marked.parse(data.response);

	const text = data.response;

	// detect Arabic
	const isArabic = /[\u0600-\u06FF]/.test(text);

	const direction = isArabic ? "rtl" : "ltr";

	resultDiv.setAttribute("dir", direction);

	resultDiv.innerHTML = marked.parse(text);
});
