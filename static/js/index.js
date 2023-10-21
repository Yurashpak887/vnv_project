    function limitDescriptionLength() {
        const descriptionInput = document.getElementById("description");
        const charCount = document.getElementById("charCount");
        const maxLength = 40;

        function updateCharCount() {
            const currentText = descriptionInput.value.trim(); // Видаляємо пробіли з початку і кінця
            const currentLength = currentText.length;
            const remainingCharacters = maxLength - currentLength;
            charCount.textContent = `${remainingCharacters} characters remaining.`;
        }

        // Визначаємо початкову кількість символів при завантаженні сторінки
        updateCharCount();

        descriptionInput.addEventListener("input", updateCharCount);
    }

    // Викликаємо функцію при завантаженні сторінки
    window.addEventListener("DOMContentLoaded", limitDescriptionLength);