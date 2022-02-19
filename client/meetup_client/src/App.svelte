<script>
    import axios from "axios";
    import "bulma/css/bulma.min.css";

    const url = "http://localhost:5000/api/1/meetup";

    let title = "";
    let subtitle = "";
    let address = "";
    let image_url = "";
    let email = "";

    function postMeetup() {
        axios
            .post(url, {
                title: title,
                subtitle: subtitle,
                address: address,
                imageurl: image_url,
                email: email,
            })
            .then((res) => console.log(res.data))
            .catch((err) => console.log(err));
    }

</script>

<main>
    <!--  -->
    <section class="container">
        <!-- <div class="field has-addons">
            <div class="control">
              <spam class="button is-static">
                prepend
              </spam>
            </div>
            <div class="control">
              <input id="prependedtext-0" name="prependedtext-0" class="input " placeholder="placeholder" type="text">
            </div>
          </div> -->
        <div class="field">
            <div class="control">
                <input
                    id="title"
                    class="input is-medium"
                    type="text"
                    placeholder="Title"
                    bind:value={title}
                />
            </div>
        </div>

        <div class="field">
            <div class="control">
                <input
                    class="input is-medium"
                    type="text"
                    placeholder="Subtitle"
                    bind:value={subtitle}
                />
            </div>
        </div>

        <div class="field">
            <div class="control">
                <input
                    class="input is-medium"
                    type="text"
                    placeholder="Address"
                    bind:value={address}
                />
            </div>
        </div>

        <div class="field">
            <div class="control">
                <input
                    class="input is-medium"
                    type="text"
                    placeholder="Image URL"
                    bind:value={image_url}
                />
            </div>
        </div>

        <div class="field">
            <div class="control">
                <input
                    class="input is-medium"
                    type="email"
                    placeholder="Email"
                    bind:value={email}
                />
            </div>
        </div>

        <button
            class="button is-block is-dark is-fullwidth"
            on:click={postMeetup}>Submit</button
        >
        <br />
        <small><em>Meetup App.</em></small>
    </section>
</main>

<style>
    .container {
        margin-top: 6em;
        width: 20em;
    }
</style>
