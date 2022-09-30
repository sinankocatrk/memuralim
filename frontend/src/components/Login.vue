<template>
    <div class="container">
        <h1>Hello {{ msg }}</h1>
    </div>
</template>

<script>
    export default {
        name: "Login",
        data() {
            return {
                msg: "Zort"
            }
        }
    }
</script>