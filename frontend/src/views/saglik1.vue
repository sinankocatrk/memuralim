<template>
    <div class="row">
    <div class="col-md-12">
        <div>
            <h4>Kontenjanları</h4>
          </div>
        <table class="table table-hover">
            <thead>
              <tr>
                <th>Kodu</th>
                <th>Sb Kodu</th>
                <th>Kurum</th>
                <th>Şehir</th>
                <th>Kontenjan</th>
              </tr>
            </thead>    

            <tbody>        
              <tr v-for="item in hospitals">
                <td>{{ item.code }}</td>
                <td>{{ item.sbcode }}</td>
                <td>{{ item.kurum }}</td>
                <td>{{ item.city }}</td>
                <td>{{ item.cont }}</td>
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