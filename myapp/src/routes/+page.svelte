<script lang="js">
    import { onMount } from "svelte";
    import Button from '@smui/button';
    // заменить название переменной на подходящее
	let data = [{}];
    onMount(async function () {
        const response = await fetch("http://127.0.0.1:8000/sensor");
        data = await response.json(); 
    });
    function componentToHex(c) {
        var hex = c.toString(16);
        return hex.length == 1 ? "0" + hex : hex;
    }
    function rgbToHex(r, g, b) {
        return "#" + componentToHex(r) + componentToHex(g) + componentToHex(b);
    }
</script>

<svelte:head>
	<title>Sibur</title>
    <!-- Написать какое-нибудь описание вместо svelte demo app -->
	<meta name="description" content="Svelte demo app" />
</svelte:head>


<!-- Вот тут нужно убрать align center -->
<h1> 
    ESG повестка НПЗ города Свободный
</h1>
<p>
    Текст
</p>
{#each data as number}
<p style="margin-top: 100px">
    {data ? number.name : null}
</p>
<div  style="width: 100px; height: 48px; border:1px solid; border-radius:10px; margin-left: 400px;
margin-top: -50px; background: #00ff00;"> 
<p>
    {data ? number.value : null}
</p>
</div>
	{/each}

<Button>123</Button>




<style>
    h1{
        text-align: center;
    }
</style>