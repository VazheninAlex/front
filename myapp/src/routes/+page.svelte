<script>
    import { onMount } from "svelte";
    // заменить название переменной на подходящее
	let characterName = [{}];
    onMount(() => {
        fetch('http://127.0.0.1:8000/sensor')
            .then((response) => response.json())
            .then((character) => {
                characterName = character;
            })
    })
    console.log(characterName)
</script>

<svelte:head>
	<title>Sibur</title>
    <!-- Написать какое-нибудь описание вместо svelte demo app -->
	<meta name="description" content="Svelte demo app" />
</svelte:head>

{characterName ? characterName[0] : null}
<!-- Вот тут нужно убрать align center -->
<h1 align="center"> 
    ESG повестка НПЗ города Свободный
</h1>
<p>
    Текст
</p>
<p style="margin-top: 100px">
    Уровень PH
</p>
<div  style="width: 100px; height: 48px; border:1px solid; border-radius:10px; margin-left: 400px;
margin-top: -50px; background: blue;"> 
<p align="center">
    7
</p>
</div>

<p style="margin-top: 100px">
    Концентрация тяжелых металлов в почве
</p>
<div  style="width: 100px; height: 48px; border:1px solid; border-radius:10px; margin-left: 400px;
margin-top: -50px; background: blue;"> 
<p align="center">
    10%
</p>
</div>


<style>
	
</style>
