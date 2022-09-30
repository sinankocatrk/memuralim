<template>
    <div class="row">
    <div class="col-md-1">

        <div>

            <h4>Kontenjanları</h4>
          </div>
        <table class="table table-hover">
            <thead>
              <tr>
                <th></th>
                <th>Kodu</th>
                <th>Sb Kodu</th>
                <th>Kurum</th>
                <th>Şehir</th>
                <th>Kontenjan</th>
                <th></th>
              </tr>
            </thead>

            <tbody>        
              <tr>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
              </tr>
            </tbody>
          </table>


    </div>
  </div>
</template>

<script>
  import {
      MDBTable,
      MDBBtn,
      MDBBadge
  } from 'mdb-vue-ui-kit';


  export default {
      name: "saglik1",
      components: {
          MDBTable,
          MDBBtn,
          MDBBadge
      },
      data() {
          return {
              hospitals: [
                  {
                      code: "123",
                      sbcode: "678",
                      kurum: "Adana Şehir Hastanesi",
                      city: "Adana",
                      cont: "5"
                  },
                  {
                      code: "234",
                      sbcode: "789",
                      kurum: "Sivas Şehir Hastanesi",
                      city: "Sivas",
                      cont: "5"
                  },
                  {
                      code: "345",
                      sbcode: "891",
                      kurum: "İzmir Şehir Hastanesi",
                      city: "İzmir",
                      cont: "5"
                  },
                  {
                      code: "456",
                      sbcode: "912",
                      kurum: "Trabzon Şehir Hastanesi",
                      city: "Trabzon",
                      cont: "5"
                  },
                  {
                      code: "567",
                      sbcode: "123",
                      kurum: "Sakarya Şehir Hastanesi",
                      city: "Sakarya",
                      cont: "5"
                  },
              ]
          }
      }
  }
</script>