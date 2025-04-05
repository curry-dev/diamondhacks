import { Component } from '@angular/core';
import { FormControl, FormsModule } from '@angular/forms';
import { ReactiveFormsModule } from '@angular/forms';
import { ApiService } from '../../services/api.service';
import { CommonModule } from '@angular/common';
import { GoogleMapsModule } from '@angular/google-maps';

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
export class SafemapComponent {
  wherefrom = new FormControl('');
  whereto = new FormControl('');

  constructor(private _apiservice: ApiService) {}

  center = { lat: 40.712776, lng: -74.005974 }; // New York coordinates
  zoom = 12;

  getRoute() {

  }
}
