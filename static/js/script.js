const submitFormColor = function () {
    const openFile = function (e) {
        let form = e.target,
            inputColor = form.querySelector('#formCustomColor');

        if (inputColor.value){
            if (inputColor.value[0] == '#') form.submit;
            else {
                inputColor.classList.add('is-invalid')
                e.preventDefault();
            }
        }
    }
    document.querySelector('form.form-colorImg').addEventListener('submit', openFile);
}

const addInputColor = function () {
    let _i = 1;
    const inputColor = function (e) {
        const btn = e.target.closest("#addColor");
        if (!btn) return;
        let input = document.createElement('div');
        input.className = "mt-2";
        input.innerHTML = `<input class="form-control" type="text" placeholder="#000000" maxlength="7" minlength="7"
                                    required id="formCustomColor-${_i}" name="custom-color-${_i}" 
                                    aria-describedby="formCustomColorValidation-${_i}">
                            <div id="formCustomColorValidation-${_i}" class="invalid-feedback">
                                Please enter the correct code
                            </div>`;
        document.querySelector('.in-colors').append(input);
        _i++;
    }
    document.addEventListener('click', inputColor);
}