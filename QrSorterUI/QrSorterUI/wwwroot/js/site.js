$(function () {
    setInterval(function () { $("#categories").load("/Category/GetPartialView"); }, 200);
});