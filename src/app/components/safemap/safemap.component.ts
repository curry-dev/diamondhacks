import { Component } from '@angular/core';
import { FormControl, FormsModule } from '@angular/forms';
import { ReactiveFormsModule } from '@angular/forms';
import { ApiService } from '../../services/api.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-safemap',
  standalone: true,
  imports: [
    ReactiveFormsModule,
    FormsModule,
    CommonModule
  ],
  templateUrl: './safemap.component.html',
  styleUrl: './safemap.component.css'
})
export class SafemapComponent {
  wherefrom = new FormControl('');
  whereto = new FormControl('');

  constructor(private _apiservice: ApiService) {}

  getRoute() {

  }
}
