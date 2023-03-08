<script lang="js">
    import { onMount } from "svelte";
    // заменить название переменной на подходящее
	let data = [{}];
    onMount(async function () {
        const response = await fetch("http://127.0.0.1:8000/sensor");
        data = await response.json(); 
    });
     $:console.log(data)
</script>

<svelte:head>
	<title>Sibur</title>
    <!-- Написать какое-нибудь описание вместо svelte demo app -->
	<meta name="description" content="Svelte demo app" />
</svelte:head>

{data ? data[0].name : null}
<!-- Вот тут нужно убрать align center -->
<h1> 
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
    h1{
        text-align: center;
    }
</style>