function createGoal() {
  // Получаем данные формы
  const form = document.getElementById('goalForm');
  const formData = new FormData(form);

  // Прогресс-бар
  let progress = 0;
  const progressBar = document.getElementById('progressBar');
  const progressText = document.getElementById('progressText');

  const interval = setInterval(() => {
    if (progress >= 100) {
      clearInterval(interval);

      // Отправляем форму (POST)
      fetch(form.action || window.location.href, {
        method: 'POST',
        body: formData
      })
      .then(response => {
        if (response.redirected) {
          // Django вернёт редирект после успешного сохранения
          window.location.href = response.url;
        } else {
          alert('Ошибка при создании цели.');
        }
      })
      .catch(error => {
        console.error(error);
        alert('Произошла ошибка.');
      });

    } else {
      progress += 10;
      progressBar.style.width = progress + '%';
      progressText.textContent = progress + '%';
    }
  }, 100);
}

document.addEventListener('DOMContentLoaded', function() {
    flatpickr('input[name="deadline"]', {
      dateFormat: "d.m.Y",  // формат для ввода
      altInput: true,       // красивый вид
      altFormat: "d.m.Y",   // формат для отображения
      allowInput: true,     // разрешить ввод вручную
    });
  });