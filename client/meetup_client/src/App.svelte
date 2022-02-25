<script>
    import "bulma/css/bulma.min.css";
    import Header from "./UI/Header.svelte";
    import MeetupList from "./Meetups/MeetupList.svelte";

    import axios from "axios";

    const url = "http://127.0.0.1:5000/api/1/meetup";
    let meetups = [];

    let getMeetUps = async () => {
        meetups = await axios
            .get(url)
            .then((res) => res.data.meetups)
            .catch((err) => console.log(err));
        console.log(meetups);
    };
    getMeetUps(); 
</script>

<main>
    <Header />
    <div class="container mt-6">
        {#each meetups as meetup}
            <MeetupList
                title={meetup.title}
                subtitle={meetup.subtitle}
                email={meetup.email}
                address={meetup.address}
                imageurl={meetup.imageurl}
                id={meetup.id_}
            />
        {/each}
    </div>
</main>

<style>
</style>
