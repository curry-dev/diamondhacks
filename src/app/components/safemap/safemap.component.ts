import { Component, OnInit } from '@angular/core';
import { FormControl, FormsModule, ReactiveFormsModule } from '@angular/forms';
import { ApiService } from '../../services/api.service';
import { CommonModule } from '@angular/common';
import { GoogleMapsModule, MapDirectionsService } from '@angular/google-maps';

@Component({
  selector: 'app-safemap',
  standalone: true,
  imports: [
    ReactiveFormsModule,
    FormsModule,
    CommonModule,
    GoogleMapsModule
  ],
  templateUrl: './safemap.component.html',
  styleUrl: './safemap.component.css'
})
export class SafemapComponent implements OnInit {
  wherefrom = new FormControl('');
  whereto = new FormControl('');

  center = { lat: 40.712776, lng: -74.005974 };
  zoom = 15;
  directionsResults?: google.maps.DirectionsResult;



  constructor(
    private _apiservice: ApiService,
    private directionsService: MapDirectionsService
  ) {}

  ngOnInit() {
    this.getCurrentLocation();
  }

  getCurrentLocation() {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(position => {
        this.center = {
          lat: position.coords.latitude,
          lng: position.coords.longitude
        };
      }, error => {
        console.error('Error getting location:', error);
      });
    } else {
      alert('Geolocation is not supported by this browser.');
    }
  }

  getRoute() {
    const origin = this.wherefrom.value;
    const destination = this.whereto.value;

    if (!origin || !destination) {
      alert('Please enter both origin and destination.');
      return;
    }

    this.directionsService
      .route({
        origin: origin,
        destination: destination,
        travelMode: google.maps.TravelMode.DRIVING,
      })
      .subscribe({
        next: (response) => {
          this.directionsResults = response.result;
        },
        error: (error) => {
          console.error('Error fetching directions:', error);
        }
      });
  }
}
