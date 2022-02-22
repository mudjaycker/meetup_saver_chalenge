<script>
    export let title;
    export let subtitle;
    export let email;
    export let address;
    export let imageurl;
</script>

<article class="box">
    <header>
        <h1 class="title is-4">{title}</h1>
        <h2 class="subtitle is-5">{subtitle}</h2>
    </header>
    <div>
        <p class="subtitle is-6">{email}</p>
    </div>

    <div class="mimi">
        <p>{address}</p>
        <p>{imageurl}</p>
    </div>

    <footer>
        <div class="buttons-are-mediums mt-6">
            <button class="button is-warning is-light mr-3">Show Details</button
            >
            <button class="button is-link is-light">Favorite</button>
        </div>
    </footer>
</article>
