<script>
    import "bulma/css/bulma.min.css";
    import Header from "./UI/Header.svelte";
    import MeetupList from "./Meetups/MeetupList.svelte";

    import axios from "axios";

    const url = "http://127.0.0.1:5000/api/1/meetup";
    let meetups = [];

    let title = "";
    let subtitle = "";
    let address = "";
    let imageurl = "";
    let email = "";

    let getMeetUps = async () => {
        meetups = await axios
            .get(url)
            .then((res) => res.data.meetups)
            .catch((err) => console.log(err));
    };

    function setBlank() {
        title = "";
        subtitle = "";
        address = "";
        imageurl = "";
        email = "";
    }
    getMeetUps();
    const addMeetup = () => {
        axios
            .post(url, {
                title: title,
                subtitle: subtitle,
                address: address,
                imageurl: imageurl,
                email: email,
            })
            .then((res) => {
                getMeetUps();
                setBlank();
            })
            .catch((err) => console.log(err));
    };
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

    <form on:submit|preventDefault={addMeetup} action="">
        <div class="container is-max-desktop mt-6">
            <div class="field has-addons">
                <div class="control">
                    <spam class="button is-static"
                        ><p class="subtitle is-4">Title</p>
                    </spam>
                </div>
                <div class="control">
                    <input
                        bind:value={title}
                        class="input"
                        placeholder="placeholder"
                        type="text"
                    />
                </div>
            </div>

            <div class="field has-addons">
                <div class="control">
                    <spam class="button is-static">
                        <p class="subtitle is-4">Subtitle</p>
                    </spam>
                </div>
                <div class="control">
                    <input
                        bind:value={subtitle}
                        class="input"
                        placeholder="placeholder"
                        type="text"
                    />
                </div>
            </div>

            <div class="field has-addons">
                <div class="control">
                    <spam class="button is-static">
                        <p class="subtitle is-4">Email</p>
                    </spam>
                </div>
                <div class="control">
                    <input
                        bind:value={email}
                        class="input"
                        placeholder="placeholder"
                        type="email"
                    />
                </div>
            </div>

            <div class="field has-addons">
                <div class="control">
                    <spam class="button is-static">
                        <p class="subtitle is-4">Address</p>
                    </spam>
                </div>
                <div class="control">
                    <input
                        bind:value={address}
                        class="input"
                        placeholder="placeholder"
                        type="text"
                    />
                </div>
            </div>

            <div class="field has-addons">
                <div class="control">
                    <spam class="button is-static is-responsive">
                        <p class="subtitle is-4">Image URL</p>
                    </spam>
                </div>
                <div class="control">
                    <input
                        bind:value={imageurl}
                        class="input"
                        placeholder="placeholder"
                        type="text"
                    />
                </div>
            </div>

            <button
                type="submit"
                class="button is-responsive is-success is-outlined"
            >
                add</button
            >
        </div>
    </form>
</main>

<style>
</style>
