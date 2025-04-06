import { Component } from '@angular/core';
import { FormControl, FormsModule } from '@angular/forms';
import { ReactiveFormsModule } from '@angular/forms';
import { ApiService } from '../../services/api.service';
import { CommonModule } from '@angular/common';
import { GoogleMapsModule, MapDirectionsService } from '@angular/google-maps';

@Component({
  selector: 'app-feelinglucky',
  standalone: true,
  providers: [ApiService],
  imports: [
    ReactiveFormsModule,
    FormsModule,
    CommonModule,
    GoogleMapsModule
  ],
  templateUrl: './feelinglucky.component.html',
  styleUrl: './feelinglucky.component.css'
})

export class FeelingluckyComponent {
  whereto = new FormControl('');
  budget = new FormControl('');
  numpeople = new FormControl('');

  center = { lat: 40.712776, lng: -74.005974 };
  zoom = 15;
  directionsResults?: google.maps.DirectionsResult;

  constructor(private _apiservice: ApiService) {}

  getTrip() {
    
  }
}
