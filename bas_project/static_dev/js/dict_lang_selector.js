document.addEventListener('DOMContentLoaded', function() {
    const sourceSelector = document.getElementById('source-lang');
    const targetSelector = document.getElementById('target-lang');
    const swapBtn = document.querySelector('.swap-langs-btn');
    
    // Инициализация селекторов
    initLangSelector(sourceSelector);
    initLangSelector(targetSelector);
    
    // Функция инициализации одного селектора
    function initLangSelector(selector) {
        const current = selector.querySelector('.dict-lang-current');
        const dropdown = selector.querySelector('.dict-lang-dropdown');
        const selected = selector.querySelector('.dict-lang-selected');
        const items = selector.querySelectorAll('.dict-lang-item');
        
        current.addEventListener('click', function(e) {
            e.stopPropagation();
            document.querySelectorAll('.dict-lang-dropdown').forEach(d => {
                if (d !== dropdown) d.style.display = 'none';
            });
            dropdown.style.display = dropdown.style.display === 'block' ? 'none' : 'block';
        });
        
        items.forEach(item => {
            item.addEventListener('click', function() {
                const lang = this.getAttribute('data-lang');
                const otherSelector = selector === sourceSelector ? targetSelector : sourceSelector;
                const otherLang = otherSelector.querySelector('.dict-lang-selected').textContent;
                
                // Проверка на совпадение языков
                if (this.textContent === otherLang) {
                    // Если языки совпадают - меняем их местами
                    swapLanguages();
                } else {
                    // Иначе просто устанавливаем выбранный язык
                    selected.textContent = this.textContent;
                    dropdown.style.display = 'none';
                }
            });
        });
    }
    
    // Функция смены языков местами
    function swapLanguages() {
        const sourceLang = sourceSelector.querySelector('.dict-lang-selected');
        const targetLang = targetSelector.querySelector('.dict-lang-selected');
        const temp = sourceLang.textContent;
        
        sourceLang.textContent = targetLang.textContent;
        targetLang.textContent = temp;
        
        // Закрываем все выпадающие списки
        document.querySelectorAll('.dict-lang-dropdown').forEach(d => {
            d.style.display = 'none';
        });
    }
    
    // Обработчик кнопки смены языков
    swapBtn.addEventListener('click', swapLanguages);
    
    // Закрытие dropdown при клике вне их
    document.addEventListener('click', function() {
        document.querySelectorAll('.dict-lang-dropdown').forEach(d => {
            d.style.display = 'none';
        });
    });
});