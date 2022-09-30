<template>

    <MDBNavbar position="top" class="nav" light bg="light" expand="lg" container>
        <MDBNavbarBrand href="/" active>memuralim</MDBNavbarBrand>    
        <MDBNavbarToggler target="navbarNav"></MDBNavbarToggler>
        <MDBNavbarNav collapse="navbarNav">
            <MDBNavbarItem to="/saglik1"> Sağlık 2020 </MDBNavbarItem>
            <MDBNavbarItem to="/saglik2"> Sağlık 2021 </MDBNavbarItem>
            <MDBNavbarItem to="/saglik3"> Sağlık Taban Puanlar </MDBNavbarItem>
        </MDBNavbarNav>
  </MDBNavbar>

</template>

<script>
    import {
        MDBNavbar,
        MDBNavbarToggler,
        MDBNavbarBrand,
        MDBNavbarNav,
        MDBNavbarItem,
    } from 'mdb-vue-ui-kit';

    export default {
        components: {
            MDBNavbar,
            MDBNavbarToggler,
            MDBNavbarBrand,
            MDBNavbarNav,
            MDBNavbarItem,
        },
    }
</script>

<style>
    
</style>