import { Component } from '@angular/core';
import { FormControl, FormsModule } from '@angular/forms';
import { ReactiveFormsModule } from '@angular/forms';
import { ApiService } from '../../services/api.service';
import { CommonModule } from '@angular/common';
import { GoogleMapsModule, MapDirectionsService } from '@angular/google-maps';

@Component({
  selector: 'app-plantrip',
  standalone: true,
  providers: [ApiService],
  imports: [
    ReactiveFormsModule,
    FormsModule,
    CommonModule,
    GoogleMapsModule
  ],
  templateUrl: './plantrip.component.html',
  styleUrl: './plantrip.component.css'
})

export class PlantripComponent {
  whereto = new FormControl('');
  budget = new FormControl('');
  numpeople = new FormControl('');

  center = { lat: 40.712776, lng: -74.005974 };
  zoom = 15;
  directionsResults?: google.maps.DirectionsResult;

  constructor(private _apiservice: ApiService) {}

  getTrip() {
    // const origin = this.wherefrom.value;
    // const destination = this.whereto.value;

    // if (!origin || !destination) {
    //   alert('Please enter both origin and destination.');
    //   return;
    // }

    // this.directionsService
    //   .route({
    //     origin: origin,
    //     destination: destination,
    //     travelMode: google.maps.TravelMode.DRIVING,
    //   })
    //   .subscribe({
    //     next: (response) => {
    //       this.directionsResults = response.result;
    //     },
    //     error: (error) => {
    //       console.error('Error fetching directions:', error);
    //     }
    //   });
  }
}
