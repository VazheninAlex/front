<script lang="js">
    const { palette } = createTheme();
    const { augmentColor } = palette;

    import { onMount } from "svelte";
    import Button from '@smui/button';
	let data = [{"name":"pH","value":1,"normalValue":7,"minValue":0,"maxValue":14,"colour":0.42857142857142855},{"name":"sensor2","value":27,"normalValue":50,"minValue":0,"maxValue":100,"colour":0.23},{"name":"sensor3","value":14,"normalValue":50,"minValue":0,"maxValue":100,"colour":0.36}];
    onMount(async function () {
        const response = await fetch("http://127.0.0.1:8000/sensor");
        data = await response.json(); 
        console.log(data);
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

{data.length}
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
<Button>
    {data ? number.value : null}
</Button>
</div>
	{/each}

<Button color={augmentColor({ color: { main: '#F40B27'} })} variant="raised">123</Button>




<style>
    h1{
        text-align: center;
    }
    .num{
        text-align: center;
    }
</style>