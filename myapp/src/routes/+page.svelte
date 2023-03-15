<script lang="js">
    import { onMount } from "svelte";
    import { Button, SvelteUIProvider } from "@svelteuidev/core";
	let data = [{"name":"pH","value":7,"normalValue":7,"minValue":0,"maxValue":14,"colour":0.0},{"name":"sensor2","value":27,"normalValue":50,"minValue":0,"maxValue":100,"colour":0.23},{"name":"sensor3","value":14,"normalValue":50,"minValue":0,"maxValue":100,"colour":0.36}];
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
	<meta name="description" content="Показатели окружающей среды города Свободный " />
</svelte:head>

<SvelteUIProvider>
    <h1> 
        ESG повестка ГХК города Свободный
    </h1>
    <p class="des">
        За последние десять лет ESG-повестка заняла важное место в международной бизнес-среде. На принципы устойчивого развития обратили внимание государственные институты, крупные компании и общество в целом. 
        Компания СИБУР внедрила ESG повестку на своих производствах одной из первых в России.
        В городе Свободный Амурской области строится новое предприятие СИБУРа Амурский газохимический комплекс.
        На нашем сайте каждый может найти данные о состоянии окружающей среды в городе Свободный: уровень Ph воды, концентрацию тяжелых металлов в почве и воздухе и тд.
    </p>
    {#each data as number}
    <h3 class="name">
        {data ? number.name : null}
    </h3>
    <div style="width: 100px; height: 50px; margin-left: 400px; margin-top: -50px;">
        <Button override={{ bc: rgbToHex(Math.round(255*2*number.colour) , Math.round(255*(1-2*number.colour)), 0), color: '#000000', '&:hover': { bc: rgbToHex(Math.round(255*2*number.colour), Math.round(255*(1-2*number.colour)), 0) }}} variant='outline'>
            {data ? number.value : null}
        </Button>
    </div>
        {/each}
</SvelteUIProvider>



<style>
    h1{
        text-align: center;
    }
    .num{
        text-align: center;
    }
    .des{
        margin-left: 2.5%;
        font-size: 18px;
    }
    .name{
        margin-top: 7.5%;
        margin-left: 2.5%;
    }
    .Button{
        min-height:1000px; 
        min-width: 2000px;
    }
</style>