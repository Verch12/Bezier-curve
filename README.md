<h1 align="center"><a href="https://ru.wikipedia.org/wiki/%D0%9A%D1%80%D0%B8%D0%B2%D0%B0%D1%8F_%D0%91%D0%B5%D0%B7%D1%8C%D0%B5">Кривая Безье</a></h1>
<h3 align="center">Привет<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="18"/>, это мой школьный проект.</h3>
<h6 align="center">10 класс</h6>

<p><b>В этой статье 3 разных вида генерации кривой безье.</b></p>

<ol>
    <li><p><b>Первый генератор <a href="https://github.com/Verch12/Bezier-curve/blob/master/bezier_curve.py">"bezier_curve.py"</a></b> создает статичную квадратичную кривую. Изменяя параметры <b>"P0,P1,P2"</b> в коде, можно изменять положение и угол кривой. Так же если изменять <b>"t"</b>, но <b>не должно "t = 1"</b>, этот параметр отвечает за частоту отрисовки точек.</p></li>
    <li><b>Второй генератор <a href="https://github.com/Verch12/Bezier-curve/blob/master/bezier_curve_2.py">"bezier_curve_2.py"</a></b> создает кривую высшей степени. Чтобы начать отрисовывать кривую нужно 1 раз и более в любом месте нажать <b>ЛКМ</b>, а чтобы стереть кривую нужно нажать <b>ПКМ</b>. Так же как и в первом случаи можно изменять <b>"t"</b> в коде.</li>
    <li><b>Третий генератор чуть интереснее чем другие. <a href="https://github.com/Verch12/Bezier-curve/blob/master/tabl_bezier_curve.py">"tabl_bezier_curve.py"</a></b> создает таблицу на базе первой кривой. Высота сталбцов выбирается случайно.</li>
</ol>
<h3 align="center">Как запустить кривую Безье.</h3>
<p>Для запуска кривой нужно дополнительно <b>установить библиотеку <a href="https://pypi.org/project/pygame/">"pygame"</a></b> и естественно нужен сам <b><a href="https://www.python.org/">python</a></b>. После того как установили библиотеку запускаем любой скрипт, либо через <b>IDE</b>, либо через <b>консоль</b>.</p>
<p>Чтобы запустить через консоль нужно открыть папку с python файлом в <b>cmd</b> и прописать следующее <b>"python 'название файла в формате .py' "</b> после чего нажать <b>ENTER</b>.</p>
<p>Есть ещё способ запуска <a href="https://github.com/Verch12/Bezier-curve/blob/master/bezier_curve_2.py">"bezier_curve_2.py"</a></b>. В папке <b>dist</b> находится <a href="https://github.com/Verch12/Bezier-curve/tree/master/dist">"bezier_curve_2.exe"</a></b> просто запускаем всё.</p>